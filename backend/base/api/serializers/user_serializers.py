from rest_framework import serializers
from base.models import Reservation

class UserReservationDataGridSerializer(serializers.ModelSerializer):

    car_name = serializers.SerializerMethodField()
    worker_name = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    saloon_name = serializers.SerializerMethodField()
    saloon_city = serializers.SerializerMethodField()

    class Meta:
        model = Reservation
        fields = ['id', 'date', 'time', 'car_name', 'worker_name', 'customer_name', 'saloon_name', 'saloon_city']

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
    
    def get_saloon_name(self, obj):
        return obj.car.saloon.name if obj.car.saloon else None

    def get_saloon_city(self, obj):
        return obj.car.saloon.address.city if obj.car.saloon else None