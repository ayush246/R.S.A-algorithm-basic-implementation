from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [# when someone enters the url of this site it passes through here
    path('ayush/', admin.site.urls), # checks if the entered url matches any of our paths
    path("",views.home),# function in views.py
    path("encrypt/",views.encrypt,name="encrypt")
]                     
