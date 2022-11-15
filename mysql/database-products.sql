use db;


CREATE TABLE products(
    ProductID int not null AUTO_INCREMENT,
    ProductName varchar(60) not null,
    ProductPrice decimal(2,2) not null,
    PRIMARY KEY (ProductID)
);

INSERT INTO products(ProductName,ProductPrice)
VALUES ("Credit card 1", 0.25),("Credit card 2",0.57);