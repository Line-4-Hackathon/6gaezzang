from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('show/', show, name="show"),
    path('<int:pk>', detail, name="detail"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('edit/<str:pk>', edit, name="edit"),
    path('update/<str:pk>', update, name="update"),
    path('delete/<str:id>', delete, name="delete"),
]