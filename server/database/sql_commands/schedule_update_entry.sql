UPDATE 'schedule'
SET _subject = :_subject, _new_subject = :_new_subject, _new_teacher = :_new_teacher,
    _new_room = :_new_room, _origin = :_origin, _treatment = :_treatment, _note = :_note
WHERE _id = :_id;
