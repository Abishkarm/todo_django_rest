from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView

from .models import ResourceType, Resource, Vendor, Purchase
from .serializer import *
from rest_framework.response import Response
from rest_framework import status,filters
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import AllowAny,DjangoModelPermissions
# from rest_framework import api_view
# Create your views here.
class ResourceTypeView(ModelViewSet):
    queryset=ResourceType.objects.all()
    serializer_class=ResourceTypeSerializer


class ResourceView(GenericAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer
    filterset_fields=['type','department']
    search_fields=['name','description']
    def get(self,request):
        queryset=self.get_queryset()
        filtered_queryset=self.filter_queryset(queryset)
        Serializer=self.serializer_class(filtered_queryset,many=True)
        return Response(Serializer.data)

    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid(): 
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)
        
class ResourceDetailView(GenericAPIView):
    queryset=Resource.objects.all()
    serializer_class=ResourceSerializer
    # permission_classes=[]

    def get(self,request,pk):
        try:
            resource_obj=Resource.objects.get(id=pk)
        except:
            return Response('Data Not found!',status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(resource_obj)
        return Response(serializer.data)
    
    def put(self,request,pk):
        try:
            resource_obj=Resource.objects.get(id=pk)
        except:
            return Response('Data Not found!',status=status.HTTP_404_NOT_FOUND)
        serializer=self.serializer_class(resource_obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data updated")
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        try:
            resource_obj=Resource.objects.get(id=pk)
        except:
            return Response('Data Not found!',status=status.HTTP_404_NOT_FOUND)
        resource_obj.delete()
        return Response('data deleted')
    
@api_view(['POST',]) 
def register(request):
    password=request.data.get('password')
    hash_password=make_password(password)
    request.data['password']=hash_password
    
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User Created")
    else:
        return Response(serializer.errors)

@api_view(['POST',]) 
@permission_classes([AllowAny])
def login(request):
    email=request.data.get('email')
    password=request.data.get('password')

    user=authenticate(username=email,password=password)

    if user==None:
        return Response("Username or password invalid",status=status.HTTP_400_BAD_REQUEST)
    else:
        token,_=Token.objects.get_or_create(user=user)
    return Response(token.key)

class VendorView(GenericAPIView):
        queryset=Vendor.objects.all()
        serializer_class=VendorSerializer

        def get(self,request):
            queryset=self.get_queryset()
            Serializer=self.serializer_class(queryset,many=True)
            return Response(Serializer.data)
        
        def post(self,request):
            data=request.data
            serializer=self.serializer_class(data=data)
            if serializer.is_valid(): 
                serializer.save()
                return Response('Data Created')
            else:
                return Response(serializer.errors)
            
        
class PurchaseView(GenericAPIView):
    queryset=Purchase.objects.all()
    serializer_class=PurchaseSerializer

    def get(self,request):
        queryset=self.get_queryset()
        serializer=self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid(): 
            serializer.save()
            return Response('Data Created')
        else:
            return Response(serializer.errors)



# @api_view
#  def register(request):
