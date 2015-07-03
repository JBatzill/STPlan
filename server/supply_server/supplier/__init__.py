from database import submit_until_db
from database.sql_commands import SQL_UPDATE_NKEY, SQL_INSERT
import requests


class BaseSupplier:
    def get_name(self):
        return "UNKNOWN"

    def submit_entry(self, db, param):
        count = submit_until_db(db, [(SQL_UPDATE_NKEY, param), (SQL_INSERT, param)])

    def update(self, db):
        raise NotImplementedError()

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
