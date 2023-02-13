from django.db import models

# Create your models here.


class Job(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=350)
    is_published = models.BooleanField()


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
