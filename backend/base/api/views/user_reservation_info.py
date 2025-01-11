from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from base.models import Reservation, CustomUser
from base.api.serializers.user_serializers import UserReservationDataGridSerializer

class GetUserReservationInfoView(APIView):
    def post(self, request):

        user_id = request.data.get('user_id')

        if not user_id:
            return Response(
                {"error": "User ID is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Fetch the user
        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "User not found."},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Check if the reservation_deleted flag is True
        if user.reservation_deleted:
            # Return the information about the deleted reservation status
            user.reservation_deleted = False  # Reset the flag
            user.save()

            return Response(
                {"reservation_deleted": True},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"reservation_deleted": False},
                status=status.HTTP_200_OK,
            )