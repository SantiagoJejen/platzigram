"""
De la clase 6; 
https://docs.djangoproject.com/en/2.0/topics/http/urls/ 
documentcion de URS
"""
"""Platzigram URLS module"""

from django.contrib import admin
from django.urls import path
from platzigram import views as local_views 
from posts import views as posts_views


urlpatterns = [
    
    path('hello-word/',local_views.hello_word),
    path('sorted/',local_views.sorted),
    path('hi/<str:name>/<int:age>/',local_views.hi),
    path('posts/',posts_views.list_posts )

]
