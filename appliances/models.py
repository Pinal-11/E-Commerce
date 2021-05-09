from django.db import models


# Create your models here.

class tv(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    screen_type = models.CharField(max_length=10)
    screen_size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class air_conditioners(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    Type = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class fridge(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    Type = models.CharField(max_length=30)
    color = models.CharField(max_length=15)
    offer = models.BooleanField(default=False)


class wm(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    Type = models.CharField(max_length=30)
    capacity = models.CharField(max_length=10)
    color = models.CharField(max_length=15)
    offer = models.BooleanField(default=False)
