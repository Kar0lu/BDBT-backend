from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Saloon, Brand, Model
from base.api.serializers.custom_serializers import SaloonPickerSerializer, ModelPickerSerializer, BrandPickerSerializer

class GetSaloonPickerView(APIView):
    def get(self, request):
        saloons = Saloon.objects.all()
        serializer = SaloonPickerSerializer(saloons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetBrandPickerView(APIView):
    def post(self, request):
        brands = Brand.objects.all()
        serializer = BrandPickerSerializer(brands, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetModelPickerView(APIView):
    def post(self, request):
        brand_id = request.data.get('brand_id')
        if brand_id:
            models = Model.objects.filter(brand_id=brand_id)
        else:
            models = Model.objects.all()
        serializer = ModelPickerSerializer(models, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)