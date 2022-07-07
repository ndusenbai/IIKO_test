from rest_framework import serializers
from .models import *

class MemberApi(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
