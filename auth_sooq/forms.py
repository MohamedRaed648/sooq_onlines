from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Sign_up_form(UserCreationForm):
    email=forms.EmailField(max_length=40,required=True,widget=forms.EmailInput())
    first_name=forms.CharField(max_length=10,required=False)
    last_name=forms.CharField(max_length=10,required=False)

    class Meta:
        model=User
        fields={"username","email","first_name","last_name"}

class Login_form(UserCreationForm):
    class Meta:
        model=User
        fields={"username","password1"}

