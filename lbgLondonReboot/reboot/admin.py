# Import your models.
from django.contrib import admin
from .models import Product, Input

# Adding models to the admin interface.
admin.site.register(Product)
admin.site.register(Input)