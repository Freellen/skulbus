from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from skulbus_api.serializers import StudentTripSerializer
from skulbus_students.models import StudentTrip


class StudentTripCreateView(generics.CreateAPIView):
    queryset = StudentTrip.objects.all()
    serializer_class = StudentTripSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        if not is_many:
            return super(StudentTripCreateView, self).create(request, *args, **kwargs)

        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()
