from django.db import models


# Create your models here.

class laptops(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    ram_size = models.CharField(max_length=10)
    processor = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class mobiles(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    ram_size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class speakers(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class cameras(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)
