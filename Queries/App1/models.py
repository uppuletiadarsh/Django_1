from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    employee_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department_id = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

