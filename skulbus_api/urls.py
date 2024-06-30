from django.urls.conf import path

from skulbus_api.views import LoginAPI, UserDetailAPI, StudentTripHistoryAPI, RouteAPI, \
    BusStopAPI
from skulbus_api.views.student_trip import StudentTripAPI
from skulbus_api.views.trip import StudentTripCreateView

app_name = "skulbus_api"

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/user/', UserDetailAPI.as_view(), name='api-user-detail'),
    path('api/trip/', StudentTripCreateView.as_view(), name='api-create-trip'),
    path('api/route/', RouteAPI.as_view(), name='api-route'),
    path('api/bus-stop/', BusStopAPI.as_view(), name='api-bus-stop'),
    path('api/student-trip/', StudentTripAPI.as_view(), name='api-student-trip'),
    path('api/trip-history/', StudentTripHistoryAPI.as_view(), name='api-trip-history'),
]