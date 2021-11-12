from django.contrib import admin
from django.urls import path
from .views import *
from drinking import views

urlpatterns = [
    path('<str:pk>/mypage/', views.MemberDetailView.as_view(), name='mypage'),
    path('developer/', developer, name="developer"),
    path('course/', course, name="course"),
    path('course2/', course2, name="course2"),
    path('mountation/', mountation, name="mountation"),
    path('weather/', weather, name="weather"),
]