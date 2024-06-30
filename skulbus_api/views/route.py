from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from skulbus_api.serializers import RouteSerializer
from skulbus_routes.models import Route


class RouteAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        route_data = Route.objects.all()
        print(route_data)
        serializer = RouteSerializer(route_data, many=True)
        return Response(serializer.data)
