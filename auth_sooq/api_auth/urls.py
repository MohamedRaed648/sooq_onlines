from sooq.api_sooq import views
from django.urls import path
from auth_sooq.api_auth.views import register_ser
from rest_framework.authtoken.views import obtain_auth_token

app_name='auth_sooq'
urlpatterns=[
    path('register',register_ser,name='register'),
    path('login',obtain_auth_token,name='login')
]