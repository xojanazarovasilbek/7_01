from rest_framework import serializers
from .models import Ichimliklar


class IchimlikSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Ichimliklar
        fields = '__all__'