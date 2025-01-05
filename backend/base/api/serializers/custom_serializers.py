from rest_framework import serializers
from base.models import Saloon, Worker, Car, Reservation, CustomUser

class SaloonPickerSerializer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField()

    class Meta:
        model = Saloon
        fields = ['id', 'name', 'city']

    def get_city(self, obj):
        return obj.address.city if obj.address else None

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

class ReservationDataGridSerializer(serializers.ModelSerializer):

    car_name = serializers.SerializerMethodField()
    worker_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'date', 'time', 'car', 'car_name', 'worker', 'worker_name', 'customer', 'customer_name']

    def get_car_name(self, obj):
        return obj.car.model.brand.name + ' ' + obj.car.model.name if obj.car else None

    def get_worker_name(self, obj):
        return obj.worker.name + ' ' + obj.worker.lastname if obj.worker else None

    def get_customer_name(self, obj):
        return obj.customer.first_name + ' ' + obj.customer.last_name if obj.customer else None

    def get_time(self, obj):
        return obj.date.strftime('%H:%M') if obj.date else None

    def get_date(self, obj):
        return obj.date.strftime('%d-%m-%Y') if obj.date else None