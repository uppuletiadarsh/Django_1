from django.db import models
class Register(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    UserName = models.CharField(max_length=100)
    PassWord = models.CharField(max_length=100)
    ConfirmPassword = models.CharField(max_length=100)
    Gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    Phone = models.CharField(max_length=15)