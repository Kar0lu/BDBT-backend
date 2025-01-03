from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Saloon, Worker, Car, Reservation, Address, Model, Brand
from .serializers import SaloonSerializer, WorkerSerializer, CarSerializer, ReservationSerializer, AddressSerializer, ModelSerializer, BrandSerializer, SaloonListSerializer

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

class ModelViewSet(viewsets.ModelViewSet):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class SaloonListView(APIView):
    def get(self, request):
        saloons = Saloon.objects.all()
        serializer = SaloonListSerializer(saloons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)