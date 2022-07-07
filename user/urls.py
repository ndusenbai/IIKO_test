from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('addMember/', AddMember.as_view(), name='addMember'),
    #path('details/<int:pk>', AddMember.as_view(), name='details'),
    path('register/', UserRegisterView.as_view(), name='register'),
]
