"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myBlog.settings import MEDIA_ROOT
from post import views as post_views
from index import views as index_views
from django.conf.urls import url
from django.views.static import serve
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index_views.index),
    path('post/<str:post_link>', post_views.showPost),
    path('tag/<str:tag_name>',index_views.tagsView),
    path('console/', admin.site.urls),
    path('getPost/',post_views.getPost),
    re_path('^media/(?P<path>.*)$',  serve, {"document_root":MEDIA_ROOT}, name='media'),
    path('gallery/',index_views.gallery),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

