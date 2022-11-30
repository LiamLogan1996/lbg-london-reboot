Create database db;
use db;

create table products(
    ProductID int not null AUTO_INCREMENT,
    ProductCategory varchar(100) not null,
    ProductName varchar(50) not null,
    ProductPrice FLOAT(7,2) not null,
    PRIMARY KEY (productID)
);

insert into products (ProductName,ProductPrice,ProductCategory)
VALUES('Council Tax',150.21,'Bills'),
('British Gas',150.21,'Bills'),
('Hydro Electric',150.21,'Bills'),
('Home Insurance',150.21,'Bills'),
('Direct Line Insurance',150.21,'Bills'),
('Vodafone (Broadband)',150.21,'Bills'),
('TV License',150.21,'Bills'),
('Starbucks',7.20,'MiscSpend'),
('Costa',3.40,'MiscSpend'),
('McDonalds',12.55,'MiscSpend'),
('Just Eat',54.12,'MiscSpend'),
('Just Eat',28.50,'MiscSpend'),
('Netflix',15.99,'Subscriptions'),
('Disney Plus',7.99,'Subscriptions'),
('Spotify',9.99,'Subscriptions'),
('Virgin Media',32.80,'Subscriptions'),
('Economist',7.99,'Subscriptions'),
('Runners World',5.99,'Subscriptions'),
('Tinder',14.32,'Subscriptions');
