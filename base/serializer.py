# from IMS.base import serializers
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','password']

class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResourceType
        fields='__all__'

class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Resource
        fields='__all__'

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vendor
        fields='__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Purchase
        fields='__all__'