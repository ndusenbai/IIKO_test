from django.urls import path, include
from .views import *

urlpatterns = [
    path('', APIView.as_view(), name='api'),
]