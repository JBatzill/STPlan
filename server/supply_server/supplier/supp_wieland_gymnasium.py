from supply_server.supplier import *
from datetime import date


#consts
SCHOOL_NAME = 'Wieland-Gymnasium'
WEBSITE_URL = "https://www.wieland-gymnasium.de/index.php/WG%20Termine/Vertretungsplan/"
COLUMN_ORDER = ['_date', None, '_class', '_time', '_new_teacher', '_new_subject', '_new_room',\
                '_subject', '_teacher', '_origin', '_treatment']
REPLACEMENTS = [(' >', '>'), ('<span>', ""), ('</span>', ""), ('&nbsp;', "")]

TAG_DAY_START = '<table'
TAG_DAY_END = '</table>'

TAG_ROW_START_1 = "<tr class='list odd'>"
TAG_ROW_START_2 = "<tr class='list even'>"
TAG_ROW_END = '</tr>'

TAG_CELL_START = '<td class="list">'
TAG_CELL_END = '</td>'

class SuppWielandGymnasium(BaseSupplier):
    def get_name(self):
        return SCHOOL_NAME

    def get_url(self):
        return WEBSITE_URL

    def update(self, db):
        page = download_website(WEBSITE_URL)

        #prepare, get rid of "bla' >" .... convert to "bla'>" and similar stuff
        page = replace_all(page, REPLACEMENTS)

        count = 0
        #iterate days then rows then cells
        for (d_s, d_e, d_c) in get_multiple_content(page, 0, len(page), TAG_DAY_START, TAG_DAY_END):
            dic_list = []

            for(r_s, r_e, r_c) in get_multiple_content(d_c, 0, d_e - d_s, TAG_ROW_START_1, TAG_ROW_END)\
                    + get_multiple_content(d_c, 0, d_e-d_s, TAG_ROW_START_2, TAG_ROW_END):
                dic = {'_school': SCHOOL_NAME, '_reason': ""}

                for(i, (c_s, c_e, c_c)) in enumerate(get_multiple_content(r_c, 0, r_e-r_s, TAG_CELL_START, TAG_CELL_END)):
                    if(COLUMN_ORDER[i] != None):
                        dic[COLUMN_ORDER[i]] = c_c

                dic_list += self.__enum_dics(db, dic)

            count += self.submit_entrys_day(db, dic_list, True)

        return count

    def __enum_dics(self, db, dic):
        conv = lambda s: ('0'+s)[len(s)-1:] #tests done!
        s_date = [conv(x.strip()) for x in dic['_date'].split('.')]
        dic['_date'] = str(date.today().year) + '-' + s_date[1] + '-' + s_date[0]
        dic['_class'] = replace_all(dic['_class'], [("(", ""), (")", "")])

        res = []
        for (_class, _time) in [(x.strip(), y.strip()) for x in dic['_class'].split(',') for y in dic['_time'].split('-')]:
            dic['_class'] = _class
            dic['_time'] = _time

            res += [dic.copy()]

        return res