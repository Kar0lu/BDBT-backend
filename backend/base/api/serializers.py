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

class SaloonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saloon
        fields = '__all__'

class SaloonListSerializer(serializers.ModelSerializer):

    employees = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Saloon
        fields = ['id', 'name', 'owner', 'city', 'employees']

    def get_employees(self, obj):
        return Worker.objects.filter(saloon=obj).count()
        
    def get_city(self, obj):
        # Return the city from the related Address model
        return obj.address.city if obj.address else None