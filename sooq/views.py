from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import Post_form
from django.contrib.auth.models import User
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
            return redirect(f'http://127.0.0.1:8000/Posts/{id}')
    else:
        form=Post_form()
    return render(request,'Add_Posts.html',{"form":form})


    
def Chats(request,id,prodect_name):
    Post=get_object_or_404(Posts,pk=id,type_of_prodect=prodect_name)
    chat=Chat.objects.filter(Chat_Posts_rel=id)
    print(chat)
    us=User.objects.all()

    if request.method == "POST":
        texts=request.POST["talk"]
        chates=Chat.objects.create(
            message=texts,
            who_send=request.user,
            Chat_Posts_rel=Post
        )
 

    return render(request, "Chat.html",{"us":us,"chat":chat,"Post":Post,'id':id})
    


def My_account(request,id):
    user_de=get_object_or_404(User,pk=id)
    print(user_de.first_name)
    post=Posts.objects.filter(post_create=request.user.id)
    return render(request,"Profile.html",{"user_de":user_de,'post':post})