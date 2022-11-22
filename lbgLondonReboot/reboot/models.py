# Create your models here.
from django.db import models
<<<<<<< HEAD
from django.db import connections

=======
# from django.db import connections - Required to query an external database.
>>>>>>> origin/frontend

# These models have been created locally for testing, they will need to be used in external
# database once ready. One for the spending, second for the users inputs during a session.
# To use locally you need to run - python manage.py makemigrations and python manage.py migrate.

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductCategory = models.CharField(max_length=100)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.FloatField()

    class Meta:
        verbose_name = 'Product'

<<<<<<< HEAD

class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.FloatField()

    class Meta:
        db_table = "products"

# May need to create model for the transactions ?.
# Run python manage.py migrate to initialise database.
# then python manage.py createsuperuser.
# stuart - pass11word
# python manage.py makemigrations reboot (if changing models).
# python manage.py migrate (to commit changes).
=======
    def __str__(self):
        return self.ProductName

class Input(models.Model):
    salary_input = models.FloatField(default=0)
    inflation_input = models.FloatField(default=0)

    class Meta:
        verbose_name = 'Input'

    def __float__(self):
        return self.salary_input
>>>>>>> origin/frontend
