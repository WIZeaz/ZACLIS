from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField('title',max_length=100)
    release_time=models.DateField('release_time')
    content=models.TextField('content')
    link=models.CharField('link',max_length=30)
    def __str__(self):
        return self.title

class Blogimage(models.Model):
    #博客相册
    title = models.CharField(max_length=20, verbose_name='图片标题', default='')
    path = models.ImageField(verbose_name='图片', upload_to='upload/%Y/%m', default='upload/default.jpg', max_length=100)

    class Meta:
        verbose_name = '网站相册'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title