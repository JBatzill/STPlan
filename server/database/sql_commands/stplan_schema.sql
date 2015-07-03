DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
  _school VARCHAR(64),
  _date DATE,
  _time TINYINT,
  _class VARCHAR(16),
  _subject VARCHAR(32),
  _teacher VARCHAR(32),
  _new_subject VARCHAR(32),
  _new_teacher VARCHAR(32),
  _new_room VARCHAR(32),
  _origin VARCHAR(64),
  _treatment VARCHAR(64),
  _reason VARCHAR(64),

  PRIMARY KEY(_school, _date, _class, _time, _subject)
);

CREATE UNIQUE INDEX main_index
ON schedule(_school, _date, _class);