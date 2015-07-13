DROP TABLE IF EXISTS school;
CREATE TABLE school (
  _id INTEGER,
  _name VARCHAR(128) NOT NULL,
  _shortcut VARCHAR(16) NOT NULL,
  _city VARCHAR(32) NOT NULL,
  _state VARCHAR(32),
  _country VARCHAR(32),
  _schedule_url TEXT NOT NULL,
  _username TEXT,
  _password TEXT,
  _last_update_info TEXT,

  PRIMARY KEY(_id)
);








DROP TABLE IF EXISTS schedule;
CREATE TABLE schedule (
  _id INTEGER,
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
CREATE UNIQUE INDEX index_schedule_unique
ON schedule(_school_id, _date, _class,_time,_teacher,_new_teacher);










DROP TABLE IF EXISTS notification;
CREATE TABLE notification (
  _id INTEGER,
  _school_id INTEGER,
  _date DATE,
  _title TEXT,
  _message TEXT,

  PRIMARY KEY(_id),
  FOREIGN KEY(_school_id) REFERENCES school(_id)
);








DROP TABLE IF EXISTS user;
CREATE TABLE user (
  _id INTEGER,
  _uuid VARCHAR(128),
  _reg_id TEXT,

  PRIMARY KEY(_id)
);

CREATE UNIQUE INDEX index_user_id
ON user(_uuid);
CREATE UNIQUE INDEX index_user_reg_id
ON user(_reg_id);








DROP TABLE IF EXISTS subscription;
CREATE TABLE subscription (
  _id INTEGER,
  _user_id INTEGER,
  _school_id INTEGER,
  _class VARCHAR(16) NOT NULL,

  PRIMARY KEY(_id),
  FOREIGN KEY(_user_id) REFERENCES user(_id),
  FOREIGN KEY(_school_id) REFERENCES school(_id)
);

CREATE INDEX index_sub
ON subscription(_user_id);
CREATE UNIQUE INDEX index_sub_unique
ON subscription(_user_id, _school_id, _class);