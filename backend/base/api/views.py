from rest_framework import viewsets
from base.models import Saloon, Worker, Car, Reservation, Address
from .serializers import SaloonSerializer, WorkerSerializer, CarSerializer, ReservationSerializer, AddressSerializer

class SaloonViewSet(viewsets.ModelViewSet):
    queryset = Saloon.objects.all()
    serializer_class = SaloonSerializer

class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer