from django.shortcuts import render
from django.http import HttpResponse
from post.models import *
from django.db.models import ObjectDoesNotExist
from post.views import generateList
def index(request):
    postList=post.objects.all().order_by('-modify_time','-release_time')
    return render(request,'index.html',{'postList':generateList(postList)})

def tagsView(request,tag_name):
    try:   
        t=tag.objects.get(name=tag_name)
        postList=t.post_set.all().order_by('-modify_time','-release_time')
        return render(request,'index.html',{'postList':generateList(postList)})
    except ObjectDoesNotExist:
        return HttpResponse("Error: tag "+ tag_name +" does not exist!")


def gallery(request):
    ML = image.objects.all()
    counter=0
    List0=[]
    List1=[]
    List2=[]
    for i in ML:
        if (counter%3==0):
            List0.append([i.title,'/media/'+str(i.path),i.referencePosts.all()])
        elif (counter%3==1):
            List1.append([i.title,'/media/'+str(i.path),i.referencePosts.all()])
        else:
            List2.append([i.title,'/media/'+str(i.path),i.referencePosts.all()])
        counter=counter+1
    return render(request,'gallery.html',{'List0':List0,'List1':List1,'List2':List2})