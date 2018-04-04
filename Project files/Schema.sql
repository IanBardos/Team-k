PRAGMA foreign_keys = ON;

drop table if exists LecturesTopics;
create table LecturesTopics(
  LTid integer primary key autoincrement,
  type text not null,
  Title text not null,
  Body text not null,
  Author integer not null,
  FOREIGN KEY (Author) REFERENCES user(Uid)
  );

drop table if exists Comments;
create table Comments(
  Cid integer primary key autoincrement,
  Author int not null,
  Body text not null,
  votes integer not null,
  LTid int not null,
  FOREIGN KEY (Author) REFERENCES user(Uid),
  FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
);

drop table if exists User;
create table User (
  Uid integer primary key autoincrement,
  username text not null,
  password text not null
);

drop table if exists Subcriptions;
create table Subscriptions(
  Sid integer primary key autoincrement,
  user integer not null,
  LTid integer not null,
  FOREIGN KEY (user) REFERENCES user(Uid),
  FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
);

drop table if exists Notification;
create table Notification(
  Nid integer primary key autoincrement,
  subscription integer not null,
  FOREIGN KEY (subscription) REFERENCES Subscriptions(Sid)
);

INSERT INTO User (Uid, username, password) values (1, "iwbardos", "123097");
INSERT INTO User (Uid, username, password) values (2, "test", "12345");
INSERT INTO LecturesTopics (LTid, type, Title, Body,Author) values (1, "Lecture", "Lecture 1", "Hello", 1);
INSERT INTO LecturesTopics (LTid, type, Title, Body,Author) values (2, "Topic", "Topic 1", "Hello", 1);
INSERT INTO Comments (Cid,Author, Body, votes, LTid) values (1, 2,"Here is a comment", 0, 1);
INSERT INTO Comments (Cid,Author, Body, votes, LTid) values (2, 1,"Here is a comment", 2, 2);
INSERT INTO Subscriptions (Sid, User, LTid) values (1, 1, 2);
INSERT INTO Subscriptions (Sid, User, LTid) values (2, 2, 1);
