from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns=[
    path('sgin_up',views.sgin_up,name="sign_up"),
    path('login',LoginView.as_view(template_name='login.html'),name="login"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('Change_Passowrd',auth_views.PasswordChangeView.as_view(template_name='Change_Password.html'),name="change"),
    path('Change_password/done/',auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),name='password_change_done'),



]