DROP DATABASE IF EXISTS guestbook;

CREATE DATABASE guestbook;

USE guestbook;

DROP TABLE IF EXISTS entries;

CREATE TABLE entries (
    guestName VARCHAR(255),
    content VARCHAR(255),
    entryID INT NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(entryID)
);

INSERT INTO
    entries (guestName, content)
values
    ("first guest", "I got here!");

INSERT INTO
    entries (guestName, content)
values
    ("second guest", "Me too!");
