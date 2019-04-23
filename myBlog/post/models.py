from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=30)
    release_time=models.DateField()