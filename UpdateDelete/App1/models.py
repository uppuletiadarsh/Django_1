from django.db import models

# Create your models here.
from django.db import models

class Insert(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    dept = models.CharField(max_length=20)
