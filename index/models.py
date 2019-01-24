from django.db import models
# Create your models here.


class Province(models.Model):
    name = models.CharField(max_length=10)

class City(models.Model):
    name = models.CharField(max_length=10)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

class Person(models.Model):
    name = models.CharField(max_length=10)
    living = models.ForeignKey(City, on_delete=models.CASCADE)

