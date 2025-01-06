from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Saloon, Address
from base.api.serializers.model_serializers import SaloonSerializer
from base.api.serializers.custom_serializers import SaloonDataGridSerializer

class GetSaloonsView(APIView):
    def get(self, request):
        saloons = Saloon.objects.all()
        serializer = SaloonDataGridSerializer(saloons, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditSaloonView(APIView):
    def patch(self, request):
        data = request.data
        try:
            saloon = Saloon.objects.get(id=data.get('id'))
        except Saloon.DoesNotExist:
            return Response({"error": "Saloon not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = SaloonSerializer(saloon, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateSaloonView(APIView):
    def post(self, request):
        data = request.data
        city = data.get('city')
        building_number = data.get('building_number')
        street = data.get('street')
        
        if not all([city, building_number, street]):
            return Response({"error": "Address details are incomplete."}, status=status.HTTP_400_BAD_REQUEST)

        address, created = Address.objects.get_or_create(
            city=city,
            building_number=building_number,
            street=street
        )

        saloon_data = {
            "name": data.get('name'),
            "owner": data.get('owner'),
            "address": address.id
        }

        serializer = SaloonSerializer(data=saloon_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSaloonView(APIView):
    def delete(self, request):
        try:
            selected_rows = request.data
            if not isinstance(selected_rows, list) or not selected_rows:
                return Response(
                    {"error": "Request body must be a non-empty array of IDs."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            deleted_count, _ = Saloon.objects.filter(id__in=selected_rows).delete()
            return Response(
                {"message": f"{deleted_count} saloons deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )