from django.contrib import admin
from django.urls import path, include


from .views import carDetailsView, carsListView


urlpatterns = [
    path('', carsListView.as_view(), name='cars'),
    path('<int:pk>/', carDetailsView.as_view(), name='car_details'),
]