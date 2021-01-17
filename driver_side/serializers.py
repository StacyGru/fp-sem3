from rest_framework import serializers
from .models import Driver, CarDetail, Car, Street, AvailableCar

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarDetail
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

class AvailableCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableCar
        fields = '__all__'