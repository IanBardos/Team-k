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

drop table if exists posts;
create table Posts(
  Pid integer primary key autoincrement,
  Title text not null,
  Body text not null,
  Author  integer not null,
  LTid int not null
  FOREIGN KEY (Author) REFERENCES user(Uid),
  FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
);

drop table if exists Comments;
create table Comments(
  Cid integer primary key autoincrement,
  Author int not null,
  Body text not null,
  votes integer not null,
  Pid int not null,
  FOREIGN KEY (Author) REFERENCES user(Uid),
  FOREIGN KEY (Pid) REFERENCES posts(Pid)
);

drop table if exists User;
create table User (
  Uid integer primary key autoincrement,
  username text not null,
  password text not null
);

drop table if exists Subciptions;
create table Subscriptions(
  Sid integer primary key autoincrement,
  user integer not null,
  LTid integer not null,
  FOREIGN KEY (user) REFERENCES user(Uid),
  FOREIGN KEY (LTid) REFERENCES LecturesTopics(LTid)
);

drop table if exists Notification;
create table Notifiction(
  Nid integer primary key not null,
  subscription integer not null,
  FOREIGN KEY (subscription) REFERENCES Subscriptions(Sid)
);
