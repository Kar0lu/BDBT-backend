from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Car, Brand, Model
from base.api.serializers.model_serializers import CarSerializer
from base.api.serializers.custom_serializers import CarSearchSerializer
from decimal import Decimal

class SearchCarsView(APIView):
    def post(self, request, *args, **kwargs):
        # Get search parameters from request body
        brand_id = request.data.get('brand')
        model_id = request.data.get('model')
        price_from = request.data.get('priceFrom')
        price_to = request.data.get('priceTo')

        # Prepare the query
        cars = Car.objects.all()

        # Apply filters
        if brand_id:
            cars = cars.filter(model__brand__id=brand_id)
        if model_id:
            cars = cars.filter(model__id=model_id)
        if price_from:
            cars = cars.filter(price__gte=Decimal(price_from))
        if price_to:
            cars = cars.filter(price__lte=Decimal(price_to))

        # Serialize the cars data
        serialized_cars = CarSearchSerializer(cars, many=True)

        return Response(serialized_cars.data, status=status.HTTP_200_OK)
