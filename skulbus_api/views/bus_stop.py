from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from skulbus_api.serializers import BusStopSerializer
from skulbus_routes.models import BusStop


class BusStopAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        bus_top_data = BusStop.objects.all()
        serializer = BusStopSerializer(bus_top_data, many=True)
        return Response(serializer.data)
