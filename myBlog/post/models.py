from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField('title',max_length=100)
    release_time=models.DateField('release_time')
    content=models.TextField('content','default')
    link=models.CharField('link',max_length=30)
    def __str__(self):
        return self.title
