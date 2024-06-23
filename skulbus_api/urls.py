from django.urls.conf import path

from skulbus_api.views import LoginAPI, UserDetailAPI

app_name = "skulbus_api"

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='api-login'),
    path('api/user/', UserDetailAPI.as_view(), name='api-user-detail'),
]