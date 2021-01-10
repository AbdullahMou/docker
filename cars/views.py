from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView #, RetrieveAPIView, RetrieveDestroyAPIView

from .serializer import carSerializer
from .models import car

# Create your views here.
class carsListView(ListAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializer

class carDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializer