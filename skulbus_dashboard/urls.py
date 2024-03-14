from django.conf import settings
from django.contrib import admin
from django.urls import path

from skulbus_dashboard.views import DashboardView

app_name = "skulbus_dashboard"

admin.site.site_header = settings.APP_NAME

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", DashboardView.as_view(), name="dashboard"),
]