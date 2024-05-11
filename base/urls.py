
from django.urls import path
from .views import *

urlpatterns = [
    path('resource-type/',ResourceTypeView.as_view({'get':'list','post':'create'})),
    path('resource-type/<int:pk>/',ResourceTypeView.as_view({'get':'retrieve','put':'update','delete':"destroy"})),
    path('resource/',ResourceView.as_view()),
    path('resource/<int:pk>/',ResourceDetailView.as_view()),
    path('register/',register),
    path('login/',login),
    path('vendor/',VendorView.as_view()),
    path('purchase/',PurchaseView.as_view()),



]