from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import *

# Create your views here.

def sgin_up(request):
    form=Sign_up_form()
    if request.method == "POST":
        form=Sign_up_form(request.POST)
        print(form)
        if form.is_valid:
            user=form.save()
            login(request,user)
            return redirect('home')
        else:
            form.save()
    return render(request,"sgin_up.html",{"form":form},)
        

