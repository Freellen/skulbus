from django.urls.conf import path

from skulbus_api.views import LoginAPI, UserDetailAPI
from skulbus_api.views.student_trip import StudentTripAPI
from skulbus_api.views.trip import StudentTripCreateView

app_name = "skulbus_api"

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/user/', UserDetailAPI.as_view(), name='api-user-detail'),
    path('api/trip/', StudentTripCreateView.as_view(), name='api-create-trip'),
    path('api/student-trip/', StudentTripAPI.as_view(), name='api-student-trip'),
]