from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=300)
    username=models.CharField(max_length=300,default='username')

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

class ResourceType(models.Model):
    name=models.CharField(max_length=30)

class Department(models.Model):
    name=models.CharField(max_length=30)
    floor=models.IntegerField()
    description=models.TextField()


class Resource(models.Model):
    name=models.CharField(max_length=30)
    type=models.ForeignKey(ResourceType,on_delete=models.SET_NULL,null=True)
    description=models.TextField(max_length=500)
    quantity=models.IntegerField()
    department=models.ManyToManyField(Department)

class Vendor(models.Model):
    name=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    company_name=models.CharField(max_length=30)
    contact_no=models.IntegerField()

class Purchase(models.Model):
    name=models.CharField(max_length=30)
    resource=models.ForeignKey(Resource,on_delete=models.SET_NULL,null=True)
    price=models.FloatField()
    quantity=models.IntegerField()
    description=models.TextField()
