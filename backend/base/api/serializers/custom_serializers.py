from rest_framework import serializers
from base.models import Saloon, Worker, Car, Reservation, CustomUser

class SaloonDataGridSerializer(serializers.ModelSerializer):

    employees = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()

    class Meta:
        model = Saloon
        fields = ['id', 'name', 'owner', 'city', 'employees']

    def get_employees(self, obj):
        return Worker.objects.filter(saloon=obj).count()

    def get_city(self, obj):
        return obj.address.city if obj.address else None

class SaloonPickerSerializer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField()

    class Meta:
        model = Saloon
        fields = ['id', 'name', 'city']

    def get_city(self, obj):
        return obj.address.city if obj.address else None

class CarDataGridSerializer(serializers.ModelSerializer):

    brand = serializers.SerializerMethodField()
    model = serializers.SerializerMethodField()
    saloon_name = serializers.SerializerMethodField()
    saloon_city = serializers.SerializerMethodField()
    number_of_units = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'brand', 'model', 'price', 'availability', 'saloon', 'saloon_name', 'saloon_city', 'number_of_units']

    def get_brand(self, obj):
        return obj.model.brand.name if obj.model.brand else None

    def get_model(self, obj):
        return obj.model.name if obj.model else None

    def get_saloon_name(self, obj):
        return obj.saloon.name if obj.saloon else None

    def get_saloon_city(self, obj):
        return obj.saloon.address.city if obj.saloon else None
    
    def get_number_of_units(self, obj):
        return Car.objects.filter(model=obj.model, availability=True).count()