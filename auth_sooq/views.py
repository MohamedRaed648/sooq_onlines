from django.http import request
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .forms import *
from django.http import JsonResponse
# from rest_framework.authtoken.models import Token
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token



def sgin_up(request):
    try:
       form=Sign_up_form()
       if request.method == "POST":
          form=Sign_up_form(request.POST)
          if form.is_valid:
              user=form.save()
              login(request,user)
              return redirect('home')
       
            
    except ValueError:
        print("no")
    
    return render(request,'sgin_up.html',{"form":form})



        

