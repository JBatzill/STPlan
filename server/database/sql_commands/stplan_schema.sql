DROP TABLE IF EXISTS school;
CREATE TABLE school (
  _id INTEGER NOT NULL AUTO_INCREMENT,
  _name VARCHAR(128),
  _shortcut VARCHAR(16),
  _city VARCHAR(32),
  _state VARCHAR(32),
  _country VARCHAR(32),
  _schedule_url TEXT,
  _last_update_info TEXT
);


DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
  _id INTEGER NOT NULL AUTO_INCREMENT,
  _school_id INTEGER NOT NULL,
  _date DATE NOT NULL,
  _class VARCHAR(16) NOT NULL,
  _time VARCHAR(32),
  _subject VARCHAR(32),
  _teacher VARCHAR(32),
  _new_subject VARCHAR(32),
  _new_teacher VARCHAR(32),
  _new_room VARCHAR(32),
  _origin VARCHAR(64),
  _treatment VARCHAR(64),
  _note TEXT,

  PRIMARY KEY(_id),
  FOREIGN KEY(_school_id) REFERENCES school(_id)
);

CREATE INDEX index_schedule_main
ON schedule(_school_id, _date, _class);

DROP TABLE IF EXISTS notification;
CREATE TABLE notification (
  _id INTEGER NOT NULL AUTO_INCREMENT,
  _school_id INTEGER,
  _date DATE,
  _title TEXT,
  _message TEXT,

  PRIMARY KEY(_id),
  FOREIGN KEY(_school_id) REFERENCES school(_id)
);

CREATE INDEX index_notification_main
ON notification(_school_id, _date);