from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Reservation, Car, Worker, CustomUser
from base.api.serializers.model_serializers import ReservationSerializer
from base.api.serializers.custom_serializers import ReservationDataGridSerializer

class GetReservationsView(APIView):
    def get(self, request):
        reservations = Reservation.objects.all()
        serializer = ReservationDataGridSerializer(reservations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# class CreateReservationView(APIView):
#     def post(self, request):
#         data = request.data

#         # Extract data from the request
#         date = data.get('date')
#         car_id = data.get('car')
#         worker_id = data.get('worker', None)
#         customer_id = data.get('customer')

#         # Validate required fields
#         if not all([date, car_id, customer_id]):
#             return Response({"error": "Date, Car, and Customer are required."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             # Fetch related objects
#             car = Car.objects.get(id=car_id)
#             customer = CustomUser.objects.get(id=customer_id)
#             worker = None
#             if worker_id:
#                 worker = Worker.objects.get(id=worker_id)

#             # Create the Reservation
#             reservation = Reservation.objects.create(
#                 date=date,
#                 car=car,
#                 worker=worker,
#                 customer=customer,
#             )

#             # Serialize and return the created Reservation
#             serializer = ReservationSerializer(reservation)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         except Car.DoesNotExist:
#             return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)
#         except CustomUser.DoesNotExist:
#             return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
#         except Worker.DoesNotExist:
#             return Response({"error": "Worker not found."}, status=status.HTTP_404_NOT_FOUND)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditReservationView(APIView):
    def patch(self, request):
        data = request.data
        try:
            reservation = Reservation.objects.get(id=data.get('id'))
        except Reservation.DoesNotExist:
            return Response({"error": "Reservation not found."}, status=status.HTTP_404_NOT_FOUND)

        # Fetch the worker from the request data
        worker_id = data.get('worker')
        if worker_id:
            try:
                worker = Worker.objects.get(id=worker_id)
                reservation.worker = worker
            except Worker.DoesNotExist:
                return Response({"error": "Worker not found."}, status=status.HTTP_404_NOT_FOUND)

        # Now update the reservation
        serializer = ReservationSerializer(reservation, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteReservationView(APIView):
    def delete(self, request):
        print('1')
        try:
            selected_rows = request.data
            if not isinstance(selected_rows, list) or not selected_rows:
                return Response(
                    {"error": "Request body must be a non-empty array of IDs."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            print('2')

            reservations = Reservation.objects.filter(id__in=selected_rows)
            if not reservations.exists():
                return Response(
                    {"error": "No reservations found with the provided IDs."},
                    status=status.HTTP_404_NOT_FOUND,
                )
            print('3')
            # Get users associated with the reservations
            users = set(reservations.values_list('customer', flat=True))
            print('4')
            # Update the reservation_deleted flag for those users
            CustomUser.objects.filter(id__in=users).update(reservation_deleted=True)
            print('5')

            deleted_count, _ = reservations.delete()
            return Response(
                {"message": f"{deleted_count} reservations deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
