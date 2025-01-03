from django.urls import path, include
from . import views

from .views import SaloonViewSet, WorkerViewSet, CarViewSet, ReservationViewSet, AddressViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'saloons', SaloonViewSet, basename='saloon')
router.register(r'workers', WorkerViewSet, basename='worker')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'addresses', AddressViewSet, basename='address')

urlpatterns = [
    path('get/', include(router.urls))
]