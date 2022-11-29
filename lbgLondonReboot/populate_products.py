import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'lbgLondonReboot.settings')

import django
django.setup()
from reboot.models import Product

def populate():
    product = [ {'ProductCategory': "Bills", 'ProductName': "Glasgow City Council Rent", 'ProductPrice': 464.83},
        {'ProductCategory': "Bills", 'ProductName': "Council Tax", 'ProductPrice': 150.86},
        {'ProductCategory': "Bills", 'ProductName': "British Gas", 'ProductPrice': 60.03},
        {'ProductCategory': "Bills", 'ProductName': "Hydro Electric", 'ProductPrice': 75.12},
        {'ProductCategory': "Bills", 'ProductName': "Admiral Home Insurance", 'ProductPrice': 15.80},
        {'ProductCategory': "Bills", 'ProductName': "Direct Line Insurance", 'ProductPrice': 34.23},
        {'ProductCategory': "Bills", 'ProductName': "Vodafone (Broadband)", 'ProductPrice': 25.99},
        {'ProductCategory': "Bills", 'ProductName': "TV License", 'ProductPrice': 12.00},
        {'ProductCategory': "Food", 'ProductName': "Waitrose", 'ProductPrice': 89.23},
        {'ProductCategory': "Food", 'ProductName': "Marks & Spencer", 'ProductPrice': 55.12},
        {'ProductCategory': "Food", 'ProductName': "Sainsburys", 'ProductPrice': 54.18},
        {'ProductCategory': "Food", 'ProductName': "Morrisons", 'ProductPrice': 52.12},
        {'ProductCategory': "Food", 'ProductName': "Tesco", 'ProductPrice': 61.12},
        {'ProductCategory': "Food", 'ProductName': "Aldi", 'ProductPrice': 35.12},
        {'ProductCategory': "Restaurants", 'ProductName': "Greggs", 'ProductPrice': 8.53},
        {'ProductCategory': "Restaurants", 'ProductName': "Starbucks", 'ProductPrice': 7.20},
        {'ProductCategory': "Restaurants", 'ProductName': "Costa", 'ProductPrice': 3.40},
        {'ProductCategory': "Restaurants", 'ProductName': "Greggs", 'ProductPrice': 5.82},
        {'ProductCategory': "Restaurants", 'ProductName': "McDonalds", 'ProductPrice': 12.55},
        {'ProductCategory': "Restaurants", 'ProductName': "Greggs", 'ProductPrice': 9.12},
        {'ProductCategory': "Restaurants", 'ProductName': "McDonalds", 'ProductPrice': 4.99},
        {'ProductCategory': "Restaurants", 'ProductName': "Starbucks", 'ProductPrice': 7.92},
        {'ProductCategory': "Restaurants", 'ProductName': "Costa", 'ProductPrice': 8.04},
        {'ProductCategory': "Restaurants", 'ProductName': "Greggs", 'ProductPrice': 12.11},
        {'ProductCategory': "Restaurants", 'ProductName': "McDonalds", 'ProductPrice': 9.83},
        {'ProductCategory': "Restaurants", 'ProductName': "Miller & Carter", 'ProductPrice': 80.43},
        {'ProductCategory': "Restaurants", 'ProductName': "Pizza Punks", 'ProductPrice': 48.60},
        {'ProductCategory': "Restaurants", 'ProductName': "Just Eat", 'ProductPrice': 28.50},
        {'ProductCategory': "Alcohol", 'ProductName': "The Winchester", 'ProductPrice': 14.85},
        {'ProductCategory': "Alcohol", 'ProductName': "The Crown", 'ProductPrice': 18.12},
        {'ProductCategory': "Alcohol", 'ProductName': "The Lion Inn", 'ProductPrice': 12.83},
        {'ProductCategory': "Alcohol", 'ProductName': "The Old Horse", 'ProductPrice': 16.23},
        {'ProductCategory': "Alcohol", 'ProductName': "The Swan", 'ProductPrice': 21.50},
        {'ProductCategory': "Alcohol", 'ProductName': "Kings Arms", 'ProductPrice': 19.80},
        {'ProductCategory': "Subscriptions", 'ProductName': "Netflix", 'ProductPrice': 15.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Disney Plus", 'ProductPrice': 7.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Spotify", 'ProductPrice': 9.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Virgin Media", 'ProductPrice': 32.80},
        {'ProductCategory': "Subscriptions", 'ProductName': "Economist", 'ProductPrice': 7.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Runners World", 'ProductPrice': 5.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Tinder", 'ProductPrice': 14.32},
        {'ProductCategory': "Subscriptions", 'ProductName': "Pure Gym", 'ProductPrice': 19.99}]

    for prod in product:
        category = prod['ProductCategory']
        name = prod['ProductName']
        price = prod['ProductPrice']
        add_line = Product(ProductCategory=category, ProductName=name, ProductPrice=price)
        add_line.save()

if __name__ == '__main__':
    print("Starting populating the product database . . . ")
    populate()
    print("Complete")