# -*- coding: utf-8 -*-
from supply_server.parser import *
from datetime import date
from database.controller import ctrl_school
from supply_server.parser.parser_result import ParserResult


#consts
_SCHOOL_ID = 1
_COLUMN_ORDER = ['_date', None, '_class', '_time', '_new_teacher', '_new_subject', '_new_room',\
                '_subject', '_teacher', '_origin', '_treatment']
_REPLACEMENTS = [(' colspan="2"', ""), (' >', '>'), ('<span>', ""), ('</span>', ""), ('&nbsp;', ""), ("'", '"')]
_REPLACEMENTS_MONTHS = [('januar', '1'), ('februar', '2'), ('märz', '3'), ('april', '4'), ('mai', '5'), ('juni', '6'),
                        ('juli', '7'), ('august', '8'), ('september', '9'), ('oktober', '10'), ('november', '11'), ('dezember', '12'), ]

_TAG_DAY_START = '<div class="sheet-1">'
_TAG_DAY_END = '<div class="sheet-clearer">'

_TAG_DATE_START = '<h3>'
_TAG_DATE_END = '</h3>'

_TAG_NOTIFICATION_START = '<table>'
_TAG_NOTIFICATION_END = '</table>'
_TAG_NOTIFICATION_TITLE_START = '<th>'
_TAG_NOTIFICATION_TITLE_END = '</th>'
_TAG_NOTIFICATION_ROW_START = '<tr>'
_TAG_NOTIFICATION_ROW_END = '</tr>'
_TAG_NOTIFICATION_PART_START = '<td>'
_TAG_NOTIFICATION_PART_END = '</td>'

_TAG_SCHEDULE_START = '<table class="subst">'
_TAG_SCHEDULE_END = '</table>'

_TAG_ROW_START_1 = '<tr class="list odd">'
_TAG_ROW_START_2 = '<tr class="list even">'
_TAG_ROW_END = '</tr>'

_TAG_CELL_START = '<td class="list">'
_TAG_CELL_END = '</td>'

class ParserWielandGymnasium(BaseParser):

    __name = "unknown"
    __url = "unknown"

    def __init__(self, db):
        info = ctrl_school.get_school(db, _SCHOOL_ID)
        self.__name = info["_name"]
        self.__url = info["_schedule_url"]

    def get_name(self):
        return self.__name

    def get_url(self):
        return self.__url

    def parse(self, db):
        page = download_website(self.get_url())

        # prepare, get rid of "bla' >" .... convert to "bla'>" and similar stuff
        page = replace_all(page, _REPLACEMENTS)

        res = []
        # iterate days
        for (d_s, d_e, d_c) in get_multiple_content(page, 0, len(page), _TAG_DAY_START, _TAG_DAY_END):
            pr = ParserResult()
            pr._school_id = _SCHOOL_ID
            pr._date = _parse_date(d_s, d_e, d_c)
            pr._notifications = _parse_notifications(d_s, d_e, d_c, pr._date)
            pr._schedule = _parse_schedule(d_s, d_e, d_c)

            res += [pr]

        return res


def _parse_date(d_s, d_e, d_c):
    (_, _, txt) = get_content(d_c, 0, d_e - d_s, _TAG_DATE_START, _TAG_DATE_END)
    idx = get_index_after(txt, 0, ",")
    txt = txt[idx:-4].strip()
    txt = replace_all(txt.lower(), _REPLACEMENTS_MONTHS)
    return _conv_date(txt)

def _parse_notifications(d_s, d_e, d_c, _date):
    not_list = []
    for(n_s, n_e, n_c) in get_multiple_content(d_c, 0, d_e - d_s, _TAG_NOTIFICATION_START, _TAG_NOTIFICATION_END):

        # get title
        (_, t_e, t_c) = get_content(n_c, 0, n_e - n_s,_TAG_NOTIFICATION_TITLE_START, _TAG_NOTIFICATION_TITLE_END)

        # get all messages
        for(r_s, r_e, r_c) in get_multiple_content(n_c, t_e, n_e - n_s,_TAG_NOTIFICATION_ROW_START, _TAG_NOTIFICATION_ROW_END):
            dic = {"_date": _date, "_school_id": _SCHOOL_ID, "_title": t_c.strip(), "_message": ""}

            # get all entry cells
            for(c_s, c_e, c_c) in get_multiple_content(r_c, 0, r_e-r_s, _TAG_NOTIFICATION_PART_START, _TAG_NOTIFICATION_PART_END):
                dic["_message"] += "   " + c_c.strip()

            dic["_message"] = dic["_message"].strip()

            not_list += [dic]

    return not_list

def _parse_schedule(d_s, d_e, d_c):
    dic_list = []
    # iterate different schedules
    for(s_s, s_e, s_c) in get_multiple_content(d_c, 0, d_e - d_s, _TAG_SCHEDULE_START, _TAG_SCHEDULE_END):

        # iterate rows of schedule
        for(r_s, r_e, r_c) in get_multiple_content(s_c, 0, s_e - s_s, _TAG_ROW_START_1, _TAG_ROW_END)\
                + get_multiple_content(s_c, 0, s_e-s_s, _TAG_ROW_START_2, _TAG_ROW_END):
            dic = {'_school_id': _SCHOOL_ID, '_note': ""}

            # iterate cells of entry
            for(i, (c_s, c_e, c_c)) in enumerate(get_multiple_content(r_c, 0, r_e-r_s, _TAG_CELL_START, _TAG_CELL_END)):
                if _COLUMN_ORDER[i] is not None:
                    dic[_COLUMN_ORDER[i]] = c_c

            dic_list += _enum_dics(dic)

    return dic_list

def _enum_dics(dic):
    dic['_date'] = _conv_date(dic['_date'])
    dic['_class'] = replace_all(dic['_class'], [("(", ""), (")", "")])

    res = []
    for (_class, _time) in [(x.strip(), y.strip()) for x in dic['_class'].split(',') for y in dic['_time'].split('-')]:
        dic['_class'] = _class
        dic['_time'] = _time

        res += [dic.copy()]

    return res

def _conv_date(_date):
    conv = lambda s: ('0'+s)[len(s)-1:]  # tests done!
    s_date = [conv(x.strip()) for x in _date.split('.')]
    return str(date.today().year) + '-' + s_date[1] + '-' + s_date[0]