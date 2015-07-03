UPDATE 'schedule'
    SET _teacher = :_teacher, _new_subject = :_new_subject, _new_teacher = :_new_teacher,
        _new_room = :_new_room, _origin = :_origin, _treatment = :_treatment, _reason = :_reason
    WHERE _school = :_school AND _date = :_date AND _class = :_class AND _time = :_time AND _subject = :_subject;