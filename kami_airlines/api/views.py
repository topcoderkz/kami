from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneListCreateView(generics.ListCreateAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer


class AirplaneRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
