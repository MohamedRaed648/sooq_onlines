from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.Prodect,name="home"),
    path("Posts/<int:id>",views.Post,name="Posts"),
    path("Add_Posts/<int:id>",views.Add_Post,name="Add_Posts"),
    path("Posts/<int:id>/<str:prodect_name>/Chat",views.Chats,name="Chat"),
    path("account/<int:id>/profile",views.My_account,name="profile"),
    path("Posts/<int:id>/info/<int:id2>",views.show_info_product,name="info")




]