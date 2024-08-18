
CREATE DATABASE myflaskapp;
use myflaskapp;

CREATE TABLE users (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    email varchar(255),
    username varchar(255),
    password varchar(255)
);

CREATE TABLE products (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(255),
    price int,
    quantity int);

CREATE TABLE orders (
    id int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    userName varchar(255),
    userEmail varchar(255),
    saleTotal decimal(10,2),
    date datetime default current_timestamp);


INSERT INTO users VALUES(null, "juan", "juan@gmail.com", "juan", "123"),
    (null, "maria", "maria@gmail.com", "maria", "456");

INSERT INTO products VALUES(null, "pc", "150", "10"),
    (null, "phone", "100", "20");
