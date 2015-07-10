from datetime import date

class ParserResult:
    _date = date(1993,1,23)
    _school_id = -1
    _schedule = []
    _notifications = []

    def get_date(self):
        return self._date

    def get_school_id(self):
        return self._school_id

    def get_schedule(self):
        return self._schedule

    def get_notifications(self):
        return self._notifications
