from django.urls import path
from .views import *
from user import views

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('signup', views.JoinView.as_view(), name='signup'),
    path('logout/', logout, name="logout"),
]