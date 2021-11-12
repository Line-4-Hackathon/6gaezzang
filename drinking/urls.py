from django.contrib import admin
from django.urls import path
from .views import *
from drinking import views

urlpatterns = [
    path('<str:pk>/mypage/', views.MemberDetailView.as_view(), name='mypage'),
    path('developer/', developer, name="developer"),
    path('recommend/', recommend, name="recommend"),
    path('weather/', weather, name="weather"),
]