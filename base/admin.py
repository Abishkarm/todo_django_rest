from django.contrib import admin
from .models import Department,ResourceType,User

# Register your models here.
admin.site.register(Department)
admin.site.register(ResourceType)
admin.site.register(User) 