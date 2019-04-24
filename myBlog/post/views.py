from django.shortcuts import render
from django.http import HttpResponse
from post.models import post
# Create your views here.
def showPost(request,post_name):
    thisPost=post.objects.filter(link=post_name)
    if (thisPost[0]!=None):
        s=thisPost[0].title+"<br>"+thisPost[0].content
        return HttpResponse(s)
    return HttpResponse("Error: this post is not exist!")

def postIndex(request):
    return render(request,'index.html')