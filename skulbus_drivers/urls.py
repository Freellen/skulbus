from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_drivers_admin

app_name = "skulbus_drivers"

urlpatterns = [
    path("admin/", skulbus_drivers_admin.urls),
    path("driver/", RedirectView.as_view(
        url="/skulbus_drivers/admin/skulbus_drivers/driver/"), name="driver-list"),
    path("", RedirectView.as_view(url="/skulbus_drivers/admin/"), name="home_url"),
]