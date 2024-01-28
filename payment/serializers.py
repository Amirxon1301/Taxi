from rest_framework import serializers
from .models import *


class PaymentSerializer(serializers.Serializer):
    class Meta:
        model = Payment
        fields = '__all__'