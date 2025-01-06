from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

from base.models import Saloon, Worker, Car, Reservation, Address, Model, Brand, CustomUser
from base.api.serializers.model_serializers import CustomUserSerializer
from base.api.serializers.custom_serializers import CustomUserDataGridSerializer

class GetUsersView(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserDataGridSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EditUserView(APIView):
    def patch(self, request):
        data = request.data
        try:
            user = CustomUser.objects.get(id=data.get('id'))
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        # Check if the address is present in the request and process it
        if 'city' in data and 'street' in data and 'building_number' in data:
            address_data = {
                'city': data['city'],
                'street': data['street'],
                'building_number': data['building_number'],
            }

            # Check if an address already exists in the database with the same details
            address, created = Address.objects.get_or_create(**address_data)

            # If the address is found or created, update the user's address
            user.address = address
            data['address'] = address.id  # Use the address ID in the data

        # Handle password change if present
        if 'password' in data:
            data['password'] = make_password(data['password'])

        # Use the serializer to update the user
        serializer = CustomUserSerializer(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    def post(self, request):
        data = request.data

        # Validate address data
        if (data.get('city') and data.get('building_number') and data.get('street')):
            address, created = Address.objects.get_or_create(
                city=data.get('city'),
                building_number=data.get('building_number'),
                street=data.get('street')
            )
        else:
            address = None

        # Create user
        try:
            user = CustomUser.objects.create(
                username=data['username'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name'],
                address=address,
                password=make_password(data['password']),
                is_staff=data.get('is_staff'),
            )
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    def delete(self, request):
        try:
            selected_rows = request.data
            if not isinstance(selected_rows, list) or not selected_rows:
                return Response(
                    {"error": "Request body must be a non-empty array of IDs."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            deleted_count, _ = CustomUser.objects.filter(id__in=selected_rows).delete()
            return Response(
                {"message": f"{deleted_count} users deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )