from rest_framework import serializers
from .models import *


class CarCategorySerializer(serializers.Serializer):
    class Meta:
        model = CarCategory
        fields = '__all__'

class DriverSerializer(serializers.Serializer):
    class Meta:
        model = Driver
        fields = '__all__'