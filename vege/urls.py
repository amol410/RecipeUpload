from django.contrib import admin
from django.urls import path
from vege import views 


urlpatterns = [
    path ('', views.receipes, name= 'receipes'),
    
    
]