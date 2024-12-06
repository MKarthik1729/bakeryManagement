create database bakery_management;

use bakery_management


-- Tables need to create users, inventory, sales 

-- users -- username,email,password,role
-- inventory -- product,product_id,cost,stock
-- sales -- product_id,sale_id,cost,no_of_items,date

create table Users (username varchar(20),password varchar(200), email varchar(50), role varchar(20));

insert into  users value('karthik','1234','k@gmail.com','admin');

select * from users;
