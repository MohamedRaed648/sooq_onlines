from django.shortcuts import get_object_or_404
from django.urls.resolvers import RegexPattern
from rest_framework import status
from rest_framework.fields import REGEX_TYPE
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sooq.api_sooq import serialzer
from sooq.models import *
from sooq.api_sooq.serialzer import *


@api_view(["GET"])
def Product_detail(request,id):
    try:
        show_pro=get_object_or_404(Prodects,pk=id)
        
    except Prodects.DoesNotExist:
        return Response(serialzer.error,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='GET':
        por_ser=Products_Serialzer(show_pro).data
        return Response(por_ser)

        
@api_view(["PUT"])
def Product_update(request,id):
    try:
        show_pro=get_object_or_404(Prodects,pk=id)
        
    except Prodects.DoesNotExist:
        return Response(serialzer.error,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='PUT':
        up_ser=Products_Serialzer(show_pro,data=request.data)
        if up_ser.is_valid():
            up_ser.save()
            data={'succuses':'updated was succesefull'}
            return Response(data=data)
        return Response(up_ser.data)


@api_view(["DELETE"])
def Product_Delete(request,id):
    try:
        show_pro=get_object_or_404(Prodects,pk=id)
        
    except Prodects.DoesNotExist:
        return Response(serialzer.error,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method =='DELETE':
        opraerion=show_pro.delete()
        if opraerion:
            data={"delete":'delete was sucssfull'}
        else:
            data={"failuer":'delete was insucssfull'}
        return Response(data=data)


@api_view(["POST"])
def Product_Create(request):
    if request.method == 'POST':
        pro_cre=Products_Serialzer(data=request.data)
        if pro_cre.is_valid():
            pro_cre.save()
            return Response(pro_cre.data,status=status.HTTP_201_CREATED)
        return Response(pro_cre.error,status=status.HTTP_400_BAD_REQUEST)


