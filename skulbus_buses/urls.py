from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_buses_admin

app_name = "skulbus_buses"

urlpatterns = [
    path("admin/", skulbus_buses_admin.urls),
    path("buses/", RedirectView.as_view(
        url="/skulbus_buses/admin/skulbus_buses/bus/"), name="buses-list"),
    path("", RedirectView.as_view(url="/skulbus_buses/admin/"), name="home_url"),
]