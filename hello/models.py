from django.db import models
from django.db import connections

# Create your models here.
class Product(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=100)
    ProductPrice = models.FloatField()
    class Meta:
        db_table = "products"