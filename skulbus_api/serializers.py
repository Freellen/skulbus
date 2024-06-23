from rest_framework import serializers

from skulbus_students.models import StudentTrip


class StudentTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTrip
        fields = '__all__'
