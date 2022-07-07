from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializer import *
from .models import *

class APIView(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = MemberApi
    #pagination_class = [IsAuthenticated]