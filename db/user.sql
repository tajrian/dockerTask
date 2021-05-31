CREATE DATABASE test;
use test;

CREATE TABLE appUser (
  user_id int unsigned NOT NULL AUTO_INCREMENT,
  first_name varchar(50) NOT NULL,
  last_name varchar(50) NOT NULL,
  email varchar(100) NOT NULL,
  phone_number varchar(100) NOT NULL,
  active int DEFAULT 1,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into appUser(user_id,first_name,last_name,email,phone_number,active) values
(1,'Tajrian Binta','Jahid','tajrian.jahid@newscred.com','01679350726',1),
(2,'Demo','Person','demo.person@gmail.com','01679350726',1);