from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import *
from .serializers import *

class HaydovchilarAPI(APIView):
    def get(self, request):
        haydovchilar = Driver.objects.all()
        serializer = DriverSerializer(haydovchilar, many=True)

        return Response(serializer.data)

    def post(self, request):
        haydovchi = request.data
        serializer = DriverSerializer(data=haydovchi)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class HaydovchiAPI(APIView):
    def update(self, request, pk):
        haydovchi = Driver.objects.get(id=pk)
        serializer = DriverSerializer(haydovchi, data=request.data)

        if serializer.is_valid():
            data = serializer.validated_data
            Driver.objects.filter(id=pk).update (
                fullname = data.get("fullname"),
                phone= data.get("phone"),
                car_type = data.get("car_type"),
                car_number = data.get("car_number"),
                car_category = data.get("car_category")
            )
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk):
        Driver.objects.get(id=pk).delete()
        return Response({"successful": "True"})

class CarCategoriesAPI(APIView):
    def get(self, request):
        cars = CarCategory.objects.all()
        serializer = CarCategorySerializer(cars, many=True)

        return Response(serializer.data)


