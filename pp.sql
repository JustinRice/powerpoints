CREATE DATABASE powerpoints;
\c powerpoints;


CREATE TABLE IF NOT EXISTS teams (
  id SERIAL not null, 
  school text NOT NULL,
  mascot text NOT NULL,
  class int NOT NULL,
  tracked char(1) NOT NULL,
  district text,
  confID int,
  points decimal(4,2) NOT NULL default 0.00,
  pmax decimal(4,2) NOT NULL default 0.00,
  pmin decimal(4,2) NOT NULL default 0.00,
  week1 int,
  week2 int,
  week3 int,
  week4 int,
  week5 int,
  week6 int,
  week7 int,
  week8 int,
  week9 int,
  week10 int,
  week11 int,
  week12 int,
  PRIMARY KEY(id)
);

insert into teams (school, mascot, class, tracked, district, confID) values ('xxxx', 'xx', 'x', 'Y', 'xxx', xx);