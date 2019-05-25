
from django.shortcuts import render
from django.http import HttpResponse

from myBlog.settings import MEDIA_ROOT
from post import models


from django.db.models import ObjectDoesNotExist
# Create your views here.
def showPost(request,post_link):
    try:
        thisPost=post.objects.get(link=post_link)
        s=str(thisPost.title)+"<br>"+str(thisPost.content)
        print("result=",s.find('\n'))
        s=s.replace('\n','<br>')
        return HttpResponse(s)
    except ObjectDoesNotExist:
        return HttpResponse("Error: this post does not exist!")


def postIndex(request):
    from post.models import post, Blogimage
    postList=post.objects.all()
    s=str(len(postList))+" post(s) totally: <br>"
    for i in postList:
        s=s+"<a href=\""+i.link+"\">"+i.title+" release time: "+str(i.release_time)+"</a> <br>"
    return HttpResponse(s)

def Is(request):
    from post.models import post, Blogimage
    ML = Blogimage.objects.all()
    aa = str(len(ML)) + " post(aa) totally: <br>"
    for i in ML:
       aa=aa+'<a href="/media/'+str(i.path)+'">'+i.title+'</a> <br>'
    return HttpResponse(aa)