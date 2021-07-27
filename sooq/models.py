from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Prodects(models.Model):
    name=models.CharField(max_length=40)
    discription=models.CharField(max_length=40)

class Posts(models.Model):
    type_of_prodect=models.CharField(max_length=40)
    prodect_cost=models.IntegerField(default=0)
    prd_post_rel=models.ForeignKey(Prodects,related_name="Post",on_delete=models.CASCADE)
    discripe_prodect=models.CharField(max_length=400)
    post_date=models.DateTimeField(auto_now_add=True)
    post_create=models.ForeignKey(User,related_name="Post",on_delete=models.CASCADE)


class Chat(models.Model):
    message=models.TextField(max_length=400)
    massage_date=models.DateTimeField(auto_now_add=True)
    who_send=models.ForeignKey(User,related_name="chat_posts",on_delete=models.CASCADE)
    Chat_Posts_rel=models.ForeignKey(Posts,related_name="chat_posts",on_delete=models.CASCADE)
