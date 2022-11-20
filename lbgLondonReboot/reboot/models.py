# Create your models here.
from django.db import models
from django.db import connections


class User(models.Model):
    user_id = models.AutoField(primary_key=True)

    salary_input = models.IntegerField(default=0)
    inflation_input = models.IntegerField(default=0)

    def __int__(self):
        return self.user_id


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
