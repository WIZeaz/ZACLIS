from django.contrib import admin
from .models import post
# Register your models here.
class post_display(admin.ModelAdmin):
    list_display=('title','release_time','link',)

admin.site.register(post,post_display)

