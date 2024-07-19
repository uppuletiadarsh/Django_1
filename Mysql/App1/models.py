from django.db import models

# Create your models here.
class Emp(models.Model):
    Name = models.CharField(max_length=10)
    Dept_Name = models.CharField(max_length=10)