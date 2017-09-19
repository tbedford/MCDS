DROP DATABASE IF EXISTS mcdsweb;

CREATE DATABASE IF NOT EXISTS mcdsweb DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;

USE mcdsweb;

CREATE TABLE customers (
       id INT UNSIGNED NOT NULL AUTO_INCREMENT,
       name VARCHAR(128),
       address VARCHAR(255),
       city VARCHAR(128),
       country VARCHAR(128),
       locode CHAR (3),
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
       email VARCHAR(128) NOT NULL UNIQUE,
       hashedpw VARCHAR(255),       
       firstname VARCHAR(128),
       surname VARCHAR(128),
       admin TINYINT DEFAULT 0,
       authenticated TINYINT DEFAULT 0,
       bday DATE,
       last_login_date DATETIME,
       last_login_ip INT UNSIGNED,
       PRIMARY KEY (email)
);

CREATE TABLE sessions (
       session_id INT UNSIGNED NOT NULL,
       ip INT UNSIGNED NOT NULL, /* Use SELECT INET_ATON('10.0.5.9'); to convert to INT and SELECT INET_NTOA(167773449); to convert back */
       FOREIGN KEY(email) REFERENCES users(email),
       PRIMARY KEY (session_id)
);
