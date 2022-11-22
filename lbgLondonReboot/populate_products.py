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
        {'ProductCategory': "MiscSpend", 'ProductName': "Greggs", 'ProductPrice': 8.53},
        {'ProductCategory': "MiscSpend", 'ProductName': "Starbucks", 'ProductPrice': 7.20},
        {'ProductCategory': "MiscSpend", 'ProductName': "Costa", 'ProductPrice': 3.40},
        {'ProductCategory': "MiscSpend", 'ProductName': "Greggs", 'ProductPrice': 5.82},
        {'ProductCategory': "MiscSpend", 'ProductName': "McDonalds", 'ProductPrice': 12.55},
        {'ProductCategory': "MiscSpend", 'ProductName': "Just Eat", 'ProductPrice': 45.12},
        {'ProductCategory': "MiscSpend", 'ProductName': "Just Eat", 'ProductPrice': 28.50},
        {'ProductCategory': "Subscriptions", 'ProductName': "Netflix", 'ProductPrice': 15.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Disney Plus", 'ProductPrice': 7.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Spotify", 'ProductPrice': 9.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Virgin Media", 'ProductPrice': 32.80},
        {'ProductCategory': "Subscriptions", 'ProductName': "Economist", 'ProductPrice': 7.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Runners World", 'ProductPrice': 5.99},
        {'ProductCategory': "Subscriptions", 'ProductName': "Tinder", 'ProductPrice': 14.32} ]

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