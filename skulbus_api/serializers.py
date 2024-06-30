from rest_framework import serializers

from skulbus_routes.models import Route, BusStop
from skulbus_students.models import StudentTrip


class StudentTripSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentTrip
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class BusStopSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusStop
        fields = '__all__'
