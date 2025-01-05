from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Saloon, Worker, Car, Reservation, Address, Model, Brand
from base.api.serializers.model_serializers import CarSerializer
from base.api.serializers.custom_serializers import CarDataGridSerializer, SaloonPickerSerializer

class GetCarsView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarDataGridSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetSaloonPickerView(APIView):
    def get(self, request):
        saloons = Saloon.objects.all()
        serializer = SaloonPickerSerializer(saloons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditCarView(APIView):
    def patch(self, request):
        data = request.data
        try:
            car = Car.objects.get(id=data.get('id'))
        except Car.DoesNotExist:
            return Response({"error": "Saloon not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CarSerializer(car, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateCarView(APIView):
    def post(self, request):
        data = request.data

        # Extract data from the request
        brand_name = data.get('brand')
        model_name = data.get('model')
        price = data.get('price')
        availability = data.get('availability')
        saloon_id = data.get('saloon', None)

        # Validate required fields
        if not all([brand_name, model_name, price]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Get or create the Brand
            brand, _ = Brand.objects.get_or_create(name=brand_name)

            # Get or create the Model
            model, _ = Model.objects.get_or_create(name=model_name, brand=brand)

            # Check if the Saloon exists
            saloon = None
            if saloon_id:
                try:
                    saloon = Saloon.objects.get(id=saloon_id)
                except Saloon.DoesNotExist:
                    return Response({"error": "Saloon does not exist."}, status=status.HTTP_404_NOT_FOUND)

            # Create the Car
            car = Car.objects.create(
                price=price,
                availability=availability,
                model=model,
                saloon=saloon
            )

            # Serialize and return the created Car
            serializer = CarSerializer(car)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class DeleteCarView(APIView):
    def delete(self, request):
        try:
            selected_rows = request.data
            if not isinstance(selected_rows, list) or not selected_rows:
                return Response(
                    {"error": "Request body must be a non-empty array of IDs."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            deleted_count, _ = Car.objects.filter(id__in=selected_rows).delete()
            return Response(
                {"message": f"{deleted_count} saloons deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )