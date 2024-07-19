from django.db import models

# Create your models here.
class details(models.Model):
    cid =models.IntegerField(primary_key=True)
    uname = models.CharField(max_length=15)
    psw = models.CharField(max_length=10)
    cpsw = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    qual = models.CharField(max_length=15)
    state = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phn = models.IntegerField('default')