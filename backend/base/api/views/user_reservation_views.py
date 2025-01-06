from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Reservation, Car, CustomUser, Worker
from base.api.serializers.model_serializers import ReservationSerializer
from base.api.serializers.user_serializers import UserReservationDataGridSerializer

class GetUserReservationsView(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')
        if user_id:
            reservations = Reservation.objects.filter(customer=user_id)
        else:
            reservations = None
        serializer = UserReservationDataGridSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DeleteUserReservationView(APIView):
    def delete(self, request):
        try:
            selected_rows = request.data
            if not isinstance(selected_rows, list) or not selected_rows:
                return Response(
                    {"error": "Request body must be a non-empty array of IDs."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            deleted_count, _ = Reservation.objects.filter(id__in=selected_rows).delete()
            return Response(
                {"message": f"{deleted_count} reservations deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class CreateUserReservationView(APIView):
    def post(self, request):
        data = request.data

        # Extract data from the request
        date = data.get('date')  # Should be in ISO 8601 format
        car_id = data.get('car')  # Should be a valid Car ID
        worker_id = data.get('worker')  # Can be None or a valid Worker ID
        user_id = data.get('user')  # Should be a valid CustomUser ID

        # Validate required fields
        if not all([date, car_id, user_id]):
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Validate foreign keys
            car = Car.objects.get(pk=car_id)
            user = CustomUser.objects.get(pk=user_id)
            worker = Worker.objects.get(pk=worker_id) if worker_id else None

            # Create the Reservation
            reservation = Reservation.objects.create(
                date=date,
                car=car,
                worker=worker,
                customer=user
            )

            # Serialize and return the created Reservation
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Car.DoesNotExist:
            return Response({"error": f"Car with ID {car_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except CustomUser.DoesNotExist:
            return Response({"error": f"User with ID {user_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Worker.DoesNotExist:
            return Response({"error": f"Worker with ID {worker_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Detailed error message
            return Response({"error": f"Unexpected error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)