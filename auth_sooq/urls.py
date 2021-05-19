from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('sgin_up',views.sgin_up,name="sign_up"),
    path('login',LoginView.as_view(template_name='login.html'),name="login"),
    path('logout',LogoutView.as_view(),name="logout")


]