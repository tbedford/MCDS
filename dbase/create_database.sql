DROP DATABASE IF EXISTS mcds;

CREATE DATABASE IF NOT EXISTS mcds DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE mcds;

CREATE TABLE customers (
       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
       name VARCHAR(128),
       address VARCHAR(255),
       city VARCHAR(128),
       country VARCHAR(128),
       loc VARCHAR (32),
       website VARCHAR(255),
       cats VARCHAR(255),
       services VARCHAR(255),
       other VARCHAR(255),
       comment VARCHAR(255),
       PRIMARY KEY (id)
);

CREATE TABLE contacts (
       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
       firstname VARCHAR(128),
       surname VARCHAR(128),
       position VARCHAR(128),
       email VARCHAR(128),
       landline VARCHAR(128),
       mobile VARCHAR(128),
       customer_id INT UNSIGNED, 
       PRIMARY KEY (id),
       FOREIGN KEY (customer_id) REFERENCES customers(id)
);

CREATE TABLE users (
       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
       email VARCHAR(128),
       hashedpw VARCHAR(255),       
       firstname VARCHAR(128),
       surname VARCHAR(128),
       admin TINYINT,
       authenticated TINYINT,
       bday DATE,
       last_login DATETIME,
       PRIMARY KEY (id)
);

CREATE TABLE sessions (
       id INT UNSIGNED NOT NULL,
       FOREIGN KEY(user_id) REFERENCES users(id),
       PRIMARY KEY (id)
);
