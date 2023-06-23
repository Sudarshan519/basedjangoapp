from django.db import models

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=256)
    start_time=models.TimeField()
    end_time=models.TimeField()
    address=models.CharField(max_length=256)
    