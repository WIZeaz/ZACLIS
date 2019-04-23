from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def showPost(request,post_name):
    return HttpResponse("Hello Django, the post name is: "+ str(post_name))

def postIndex(request):
    return HttpResponse("This is post index")