from django.db import models

# Create your models here.
class Details(models.Model):
    Htno = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=20)
    sub1 = models.IntegerField()
    sub2 = models.IntegerField()
    sub3 = models.IntegerField()
    Avg = models.IntegerField()
    total = models.IntegerField()