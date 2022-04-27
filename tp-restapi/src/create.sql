CREATE TABLE IF NOT EXISTS Users (
    id text PRIMARY KEY,
    firstname varchar,
    lastname varchar,
    age int,
    email varchar,
    job varchar);
CREATE TABLE IF NOT EXISTS Application (id text PRIMARY KEY,
 appname varchar,
 username varchar,
 lastconnection date,
 user_id varchar)
