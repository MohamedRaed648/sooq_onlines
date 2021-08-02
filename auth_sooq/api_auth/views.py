from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from auth_sooq.api_auth.serializer import RegisterSerializer
from rest_framework.authtoken.models import Token
@api_view(['POST'])
def register_ser(request):

    if request.method == "POST":
        serializer=RegisterSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            user=serializer.save()
            data["response"]='successfully registered a new user'
            data["email"]=user.email
            data['username']=user.username
            token=Token.objects.get(user=user).key
            data["token"]=token
        else:
            data=serializer.errors
        return Response(data)
