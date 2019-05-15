from django.db import models
from post.models import *

# Create your models here.
class tag(models.Model):
    name=models.CharField('name',max_length=50)
    description=models.CharField('description',max_length=100)
    def __str__(self):
        return self.name