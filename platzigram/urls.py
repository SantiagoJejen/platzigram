"""
De la clase 6; 
https://docs.djangoproject.com/en/2.0/topics/http/urls/ 
documentcion de URS
"""
"""Platzigram URLS module"""

from django.contrib import admin
from django.urls import path, include
from platzigram import views as local_views 
from posts import views as posts_views
from users import views as users_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    path('hello-word/',local_views.hello_word, name = 'hellow_word'),
    path('sorted/',local_views.sorted, name = 'sort'),
    path('hi/<str:name>/<int:age>/',local_views.hi, name = 'hi'),

    path('',include(('posts.urls','posts'), namespace='posts')),
    path('users/',include(('users.urls','users'), namespace='users')),

    
    path('admin/', admin.site.urls),

   

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
