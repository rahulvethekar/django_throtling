from django.db import models

# Create your models here.


class Student(models.Model):
    rn = models.IntegerField(unique=True,blank=False)
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    marks = models.IntegerField(blank=False)


class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=20)
    