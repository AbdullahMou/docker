from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView ,CreateAPIView

from rest_framework.permissions import IsAuthenticated
from .serializer import carSerializer
from .models import car

from .permissions import PermissionsClass

# Create your views here.
class carsListView(ListAPIView,CreateAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)

class carDetailsView(RetrieveUpdateDestroyAPIView):
    queryset = car.objects.all()
    serializer_class = carSerializer
    permission_classes = (PermissionsClass,IsAuthenticated)