import hashlib
from database import submit_many_db, submit_db
from database.sql_commands import SQL_SCHEDULE_DELETE_ENTRY, SQL_SCHEDULE_INSERT_ENTRY
import requests


class BaseParser:
    __md5 = "Not_Initialized"

    def submit_entrys_day(self, db, param_list, del_day=False):
        if(del_day and len(param_list) > 0):
            self.delete_day(db, param_list[0], False)
        return submit_many_db(db, SQL_SCHEDULE_INSERT_ENTRY, param_list)

    def delete_day(self, db, param, commit=True):
        submit_db(db, SQL_SCHEDULE_DELETE_ENTRY, {'_school': param['_school'], '_date': param['_date']}, commit)

    def check_for_change(self):
        new_md5 = get_md5(download_website(self.get_url()))
        if(new_md5 == self.__md5):
            return False
        else:
            self.__md5 = new_md5
            return True

    #abstract methods
    def get_name(self):
        raise NotImplementedError()

    def get_url(self):
        raise NotImplementedError()

    def parse(self, db):
        raise NotImplementedError()

#return md5 hash
def get_md5(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()


#returns code of website located at url
def download_website(url):
    res = requests.get(url)
    return res.text

#replace all
def replace_all(text, replacements):
    for (old, new) in replacements:
        text = text.replace(old, new)
    return text

#get index after sub in text starting at idx
def get_index_after(text, idx, tag):
    try:
        pos = text.index(tag, idx) + len(tag)
    except Exception:
        return -1
    return pos

GET_CONTENT_ERROR = (-1, -1, "")
#return substring of text between start_tag and end_tag, starts searching at low and stops at upp
#(left, right,content)
#(AFTER START TAG, BEFORE END TAG!!!!)
def get_content(text, low, upp, start_tag, end_tag):
    if low >= upp:
        return GET_CONTENT_ERROR

    try:
        left = text.index(start_tag, low) + len(start_tag)
    except Exception:
        return GET_CONTENT_ERROR

    try:
        right = text.index(end_tag, left)
    except Exception:
        return GET_CONTENT_ERROR

    if right + len(end_tag) > upp:
        return GET_CONTENT_ERROR
    else:
        return (left, right, text[left:right])

def get_multiple_content(text, low, upp, start_tag, end_tag):
    p = get_content(text, low, upp, start_tag, end_tag)
    if p[0] == -1:
        return []
    else:
        return [p]+get_multiple_content(text, p[1], upp, start_tag, end_tag)
