from django.urls import path, include
from . import views

from .views.model_views import SaloonViewSet, WorkerViewSet, CarViewSet, ReservationViewSet, AddressViewSet, ModelViewSet, BrandViewSet, UserViewSet
from .views.picker_views import  GetSaloonPickerView, GetBrandPickerView, GetModelPickerView
from .views.search_views import SearchCarsView

from .views.saloon_views import GetSaloonsView, CreateSaloonView, EditSaloonView, DeleteSaloonView
from .views.car_views import GetCarsView, CreateCarView, EditCarView, DeleteCarView
from .views.reservation_views import GetReservationsView, DeleteReservationView
from .views.user_views import GetUsersView, CreateUserView, EditUserView, DeleteUserView



from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'saloons', SaloonViewSet, basename='saloon')
router.register(r'workers', WorkerViewSet, basename='worker')
router.register(r'cars', CarViewSet, basename='car')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'models', ModelViewSet, basename='model')
router.register(r'brands', BrandViewSet, basename='brand')
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('test/', include(router.urls)),

    path('search/cars', SearchCarsView.as_view(), name='search-cars'),

    path('get/saloonpicker', GetSaloonPickerView.as_view(), name='get-saloon-picker'),
    path('get/modelpicker', GetModelPickerView.as_view(), name='get-model-picker'),
    path('get/brandpicker', GetBrandPickerView.as_view(), name='get-brand-picker'),

    path('get/saloons', GetSaloonsView.as_view(), name='get-saloons'),
    path('create/saloon', CreateSaloonView.as_view(), name='create-saloon'),
    path('edit/saloon', EditSaloonView.as_view(), name='edit-saloon'),
    path('delete/saloon', DeleteSaloonView.as_view(), name='delete-saloon'),

    path('get/cars', GetCarsView.as_view(), name='get-cars'),
    path('create/car', CreateCarView.as_view(), name='create-car'),
    path('edit/car', EditCarView.as_view(), name='edit-car'),
    path('delete/car', DeleteCarView.as_view(), name='delete-car'),

    path('get/reservations', GetReservationsView.as_view(), name='get-reservations'),
    # path('create/reservation', CreateReservationView.as_view(), name='create-reservation'),
    # path('edit/reservation', EditReservationView.as_view(), name='edit-reservation'),
    path('delete/reservation', DeleteReservationView.as_view(), name='delete-reservation'),

    path('get/users', GetUsersView.as_view(), name='get-users'),
    path('create/user', CreateUserView.as_view(), name='create-user'),
    path('edit/user', EditUserView.as_view(), name='edit-user'),
    path('delete/user', DeleteUserView.as_view(), name='delete-user'),

    # path('get/workers', GetSaloonsView.as_view(), name='get-saloons'),
    # path('create/worker', CreateSaloonView.as_view(), name='create-saloon'),
    # path('edit/worker', EditSaloonView.as_view(), name='edit-saloon'),
    # path('delete/worker', DeleteSaloonView.as_view(), name='delete-saloon')
]