from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    father_name = models.CharField(max_length=20)
    college = models.CharField(max_length=20)
    branch = models.CharField(max_length=20)
    pin = models.IntegerField()
    company = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    experience = models.CharField(max_length=20)
