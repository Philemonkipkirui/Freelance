from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('assistant_view/', views.assistant_view, name='assistant_view'),
    path('generate_content/', views.generate_content, name='generate_content')
]