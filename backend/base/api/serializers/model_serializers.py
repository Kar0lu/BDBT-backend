from rest_framework import serializers
from base.models import Saloon, Worker, Car, Reservation, CustomUser, Address, Model, Brand

class SaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = '__all__'

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'