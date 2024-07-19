from django.db import models

# Create your models here.
class Emp(models.Model):
    Id = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=15)
    PassWord = models.CharField(max_length=15)
    ConfirmPassword = models.CharField(max_length=15)
    Dept_Id = models.IntegerField(max_length=10)