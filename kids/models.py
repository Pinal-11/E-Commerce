from django.db import models


# Create your models here.

class b_cloth(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class g_cloth(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class b_footwear(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)


class g_footwear(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    offer = models.BooleanField(default=False)
