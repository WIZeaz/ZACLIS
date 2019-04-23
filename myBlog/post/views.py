from django.shortcuts import render
from django.http import HttpResponse
from post.models import post
# Create your views here.
def showPost(request,post_name):
    postlist=post.objects.all()
    s="Postlist:<br>"
    for i in postlist:
        s=s+"title: "+i.title+"  release time: "+str(i.release_time)+"<br>"
    return HttpResponse(s)

def postIndex(request):
    return render(request,'index.html')