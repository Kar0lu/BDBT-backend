from django.urls import path, include
from . import views

from .views import SaloonViewSet, WorkerViewSet, CarViewSet, ReservationViewSet, AddressViewSet, ModelViewSet, BrandViewSet, SaloonListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'saloons', SaloonViewSet, basename='saloon')
router.register(r'workers', WorkerViewSet, basename='worker')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'models', ModelViewSet, basename='model')
router.register(r'brands', BrandViewSet, basename='brand')

urlpatterns = [
    path('test/', include(router.urls)),
    path('get/saloons/', SaloonListView.as_view(), name='saloon-list'),
]