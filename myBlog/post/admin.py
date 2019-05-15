from django.contrib import admin
from .models import *
# Register your models here.
class post_display(admin.ModelAdmin):
    list_display=('title','release_time','link',)

admin.site.register(post,post_display)
admin.site.register(tag)

