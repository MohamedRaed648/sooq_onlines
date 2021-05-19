from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_up_form(UserCreationForm):
    email=forms.EmailField(max_length=40,required=True,widget=forms.EmailInput())
    class Meta:
        model=User
        fields={"username","email"}

class Login_form(UserCreationForm):
    class Meta:
        model=User
        fields={"username","password1"}

