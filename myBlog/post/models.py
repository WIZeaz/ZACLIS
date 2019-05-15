from django.db import models
from index.models import tag
# Create your models here.
class post(models.Model):
    title=models.CharField('title',max_length=50,primary_key=True)
    release_time=models.DateField('release_time')
    modify_time=models.DateField('modify_time')
    content=models.TextField('content')
    link=models.CharField('link',max_length=30)
    tags=models.ManyToManyField(tag)
    def __str__(self):
        return self.title

#class comment(models.Model):
#    title=models.CharField('title',max_length=50)
#    release_time=models.DateField('release_time')
#    content=models.TextField('content')
#    email=models.CharField('email',max_length=50)
#    firstChild=models.IntegerField()
#    lastChild=models.IntegerField()
#    nextBrot=models.IntegerField()