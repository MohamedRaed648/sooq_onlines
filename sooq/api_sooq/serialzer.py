from rest_framework import fields, serializers
from sooq.models import *

class Products_Serialzer(serializers.ModelSerializer):
    class Meta:
        model=Prodects
        fields='__all__'

class Posts_Serialzer(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields="__all__"


    