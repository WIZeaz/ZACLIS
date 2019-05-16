from django.db import models
# Create your models here.

class tag(models.Model):
    name=models.CharField('name',max_length=50,primary_key=True)
    description=models.CharField('description',max_length=100)
    def __str__(self):
        return self.name


class post(models.Model):
    title=models.CharField('title',max_length=50,primary_key=True)
    release_time=models.DateField('release_time')
    modify_time=models.DateField('modify_time')
    content=models.TextField('content')
    link=models.CharField('link',max_length=30)
    tags=models.ManyToManyField(tag)
    class meta:
        ordering=('modify_time',)
    def __str__(self):
        return self.title

#class comment(models.Model):
#    title=models.CharField('title',max_length=50)
#    release_time=models.DateField('release_time')
#    content=models.TextField('content')
#    email=models.CharField('email',max_length=50)
#    replyTo=models.foreignKey(comment)