Create database db;

use db;

create table products(
    ProductID int not null AUTO_INCREMENT,
    ProductCategory varchar(100) not null,
    ProductName varchar(50) not null,
    ProductPrice FLOAT(7, 2) not null,
    PRIMARY KEY (productID)
);

Insert INTO
    Products (ProductCategory, ProductName, ProductPrice)
VALUES
    ('Bills', 'Glasgow City Council Rent', 464.83),
    ('Bills', 'Council Tax', 150.86),
    ('Bills', 'British Gas', 60.03),
    ('Bills', 'Hydro Electric', 75.12),
    ('Bills', 'Admiral Home Insurance', 15.80),
    ('Bills', 'Direct Line Insurance', 34.23),
    ('Bills', 'Vodafone (Broadband)', 25.99),
    ('Bills', 'TV License', 12.00),
    ('Food', 'Waitrose', 89.23),
    ('Food', 'Marks & Spencer', 55.12),
    ('Food', 'Sainsburys', 54.18),
    ('Food', 'Morrisons', 52.12),
    ('Food', 'Tesco', 61.12),
    ('Food', 'Aldi', 35.12),
    ('Restaurants', 'Greggs', 8.53),
    ('Restaurants', 'Starbucks', 7.20),
    ('Restaurants', 'Costa', 3.40),
    ('Restaurants', 'Greggs', 5.82),
    ('Restaurants', 'McDonalds', 12.55),
    ('Restaurants', 'Greggs', 9.12),
    ('Restaurants', 'McDonalds', 4.99),
    ('Restaurants', 'Starbucks', 7.92),
    ('Restaurants', 'Costa', 8.04),
    ('Restaurants', 'Greggs', 12.11),
    ('Restaurants', 'McDonalds', 9.83),
    ('Restaurants', 'Miller & Carter', 80.43),
    ('Restaurants', 'Pizza Punks', 48.60),
    ('Restaurants', 'Just Eat', 28.50),
    ('Alcohol', 'The Winchester', 14.85),
    ('Alcohol', 'The Crown', 18.12),
    ('Alcohol', 'The Lion Inn', 12.83),
    ('Alcohol', 'The Old Horse', 16.23),
    ('Alcohol', 'The Swan', 21.50),
    ('Alcohol', 'Kings Arms', 19.80),
    ('Subscriptions', 'Netflix', 15.99),
    ('Subscriptions', 'Disney Plus', 7.99),
    ('Subscriptions', 'Spotify', 9.99),
    ('Subscriptions', 'Virgin Media', 32.80),
    ('Subscriptions', 'Economist', 7.99),
    ('Subscriptions', 'Runners World', 5.99),
    ('Subscriptions', 'Tinder', 14.32),
    ('Subscriptions', 'Pure Gym', 19.99)