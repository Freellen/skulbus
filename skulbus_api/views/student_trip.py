from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone

from skulbus_api.serializers import StudentTripSerializer
from skulbus_students.models import StudentTrip


class StudentTripAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        today = timezone.now().date()
        start_of_day = timezone.make_aware(
            timezone.datetime.combine(today, timezone.datetime.min.time()))
        end_of_day = timezone.make_aware(
            timezone.datetime.combine(today, timezone.datetime.max.time()))
        student_data = StudentTrip.objects.filter(timestamp__range=(start_of_day, end_of_day))
        serializer = StudentTripSerializer(student_data, many=True)
        return Response(serializer.data)
