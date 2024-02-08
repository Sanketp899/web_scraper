"""
URL configuration for ai_auto_fill project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_a import views
from django.urls import path, include
from app_a import models
urlpatterns = [
    path('', views.index, name='index'),
    path('result/', views.result, name='result'),
    path('admin/', admin.site.urls),
    path('create_file/', views.create_file_view, name='create_file'),
    path('about/', views.about, name='about'),
    path('services/',views.services, name='services'),
    path('contact/',views.contact, name='contact'),
    
]
