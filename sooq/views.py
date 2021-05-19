from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import Post_form,Chat_form
# Create your views here.

def Prodect(request):
    prodect_show_all=Prodects.objects.all()
    return render(request,'home.html',{"prodects":prodect_show_all})

def Post(request,id):
    post_show_all=get_object_or_404(Prodects,pk=id)
    queryset=post_show_all.User.all()
    return render(request,"Posts.html",{"post_show_all":post_show_all,"queryset":queryset})

     

def Add_Post(request,id):
    post_show_all=get_object_or_404(Prodects,pk=id)
    if request.method == "POST":
        form=Post_form(request.POST)
        if form.is_valid:
            forms=form.save(commit=False)
            forms.post_create=request.user
            forms.prd_post_rel=post_show_all
            forms.save()
    else:
        form=Post_form()
    return render(request,'Add_Posts.html',{"form":form})


    
def Chats(request,id,prodect_name):
    Post=get_object_or_404(Posts,pk=id,type_of_prodect=prodect_name)


    if request.method == "POST":
        form=Chat_form(request.POST)
        if form.is_valid:
            forms= form.save(commit=False)
            forms.who_send=request.user
            forms.Chat_Posts_rel= Post
            forms.save()
    else:
        form=Chat_form()
        print("no")
   

    return render(request, "Chat.html",{"form":form})
    


