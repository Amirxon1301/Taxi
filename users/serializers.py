from rest_framework import serializers
from .models import *


class OperatorSerializer(serializers.Serializer):
    class Meta:
        model = Operator
        fields = '__all__'

class ClientSerializer(serializers.Serializer):
    class Meta:
        model = Client
        fields = '__all__'

class OrderSerializer(serializers.Serializer):
    class Meta:
        model = Order
        fields = '__all__'

