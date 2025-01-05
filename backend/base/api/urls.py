from django.urls import path, include
from . import views

from .views.model_views import SaloonViewSet, WorkerViewSet, CarViewSet, ReservationViewSet, AddressViewSet, ModelViewSet, BrandViewSet
from .views.saloon_views import GetSaloonsView, CreateSaloonView, EditSaloonView, DeleteSaloonView
from .views.car_views import GetCarsView, CreateCarView, EditCarView, DeleteCarView, GetSaloonPickerView

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

    path('get/saloonpicker', GetSaloonPickerView.as_view(), name='get-saloon-picker'),

    path('get/saloons', GetSaloonsView.as_view(), name='get-saloons'),
    path('create/saloon', CreateSaloonView.as_view(), name='create-saloon'),
    path('edit/saloon', EditSaloonView.as_view(), name='edit-saloon'),
    path('delete/saloon', DeleteSaloonView.as_view(), name='delete-saloon'),

    path('get/cars', GetCarsView.as_view(), name='get-cars'),
    path('create/car', CreateCarView.as_view(), name='create-car'),
    path('edit/car', EditCarView.as_view(), name='edit-car'),
    path('delete/car', DeleteCarView.as_view(), name='delete-car'),

    # path('get/workers', GetSaloonsView.as_view(), name='get-saloons'),
    # path('create/worker', CreateSaloonView.as_view(), name='create-saloon'),
    # path('edit/worker', EditSaloonView.as_view(), name='edit-saloon'),
    # path('delete/worker', DeleteSaloonView.as_view(), name='delete-saloon'),

    # path('get/reservations', GetSaloonsView.as_view(), name='get-saloons'),
    # path('create/reservation', CreateSaloonView.as_view(), name='create-saloon'),
    # path('edit/reservation', EditSaloonView.as_view(), name='edit-saloon'),
    # path('delete/reservation', DeleteSaloonView.as_view(), name='delete-saloon'),

    # path('get/users', GetSaloonsView.as_view(), name='get-saloons'),
    # path('create/user', CreateSaloonView.as_view(), name='create-saloon'),
    # path('edit/user', EditSaloonView.as_view(), name='edit-saloon'),
    # path('delete/user', DeleteSaloonView.as_view(), name='delete-saloon'),

]