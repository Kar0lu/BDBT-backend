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