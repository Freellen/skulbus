from django.urls.conf import path

from skulbus_api.views import LoginAPI

app_name = "skulbus_api"

urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='api-login'),
]