from rest_framework import serializers
from .models import car

class carSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'carModel','owner', 'year')
        model = car