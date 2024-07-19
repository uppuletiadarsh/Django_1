from django.db import models

# Create your models here.
class Emp(models.Model):
    idno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=10,decimal_places=2)