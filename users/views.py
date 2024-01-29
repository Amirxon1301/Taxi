from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from driver.serializers import CustomDriverSerializer
from .serializers import *
from .models import *

class OperatorTokenView(APIView):
    @swagger_auto_schema(request_body=CustomOperatorSerializer)
    def post(self, request):
        operator = CustomUser.objects.filter(
            username = request.data.get("username"),
            password = request.data.get("password"),
            role = "Operator"
        ).first()
        if operator is None:
            return Response({"xabar":"Operator topilmadi"})
        refresh = RefreshToken.for_user(operator)
        resp = {
            "username" : request.data.get("username"),
            "access" : str(refresh.access_token),
            "refresh" : str(refresh)
        }
        return Response(resp)

class DriverTokenView(APIView):
    @swagger_auto_schema(request_body=CustomDriverSerializer)
    def post(self, request):
        driver = CustomUser.objects.filter(
            username = request.data.get("username"),
            role = "Driver"
        ).first()
        if driver is None:
            return Response({"xabar":"Driver topilmadi"})
        refresh = RefreshToken.for_user(driver)
        resp = {
            "username" : request.data.get("username"),
            "access" : str(refresh.access_token),
            "refresh" : str(refresh)
        }
        return Response(resp)

class OrderCreateAPI(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request)
        if serializer.is_valid():
            serializer.save(status="active")

            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                "order_group",
                {
                    "type": "add_new_order",
                },
            )
            return Response(serializer.data)
        return Response(serializer.errors)