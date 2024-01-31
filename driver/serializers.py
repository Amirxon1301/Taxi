from rest_framework import serializers
from .models import *
from users.models import CustomUser

class CarCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CarCategory
        fields = '__all__'

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class CustomDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]