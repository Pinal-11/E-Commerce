from django.db import models


# Create your models here.

class decoration(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class kitchen_appliance(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class home_furniture(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)
