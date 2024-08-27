from django.db import models

# Create your models here.
class Product_Akshira(models.Model):
    Product_Name = models.CharField( max_length=100)
    Product_Type = models.CharField(max_length=100)
    Product_Price = models.IntegerField(default=0)
    