from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from skulbus_api.serializers import StudentTripSerializer
from skulbus_students.models import StudentTrip


class StudentTripAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        student_data = StudentTrip.objects.filter(parent_id=user.id)
        serializer = StudentTripSerializer(student_data, many=True)
        return Response(serializer.data)
