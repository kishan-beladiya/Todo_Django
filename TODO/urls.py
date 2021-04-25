from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('register/', views.register, name="register"),
    path('loginUser/', views.loginUser, name="loginUser"),
    path('logoutUSer/', views.logoutUser, name="logoutUser"),
    path('delete/<int:pk>/', views.delete, name="delete"),
]
