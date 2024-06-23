from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_drivers_admin
from .views import DriversListView
from .views.drivers_view import register_drivers

app_name = "skulbus_drivers"

urlpatterns = [
    path("admin/", skulbus_drivers_admin.urls),
    # path("driver/", RedirectView.as_view(
    #     url="/skulbus_drivers/admin/skulbus_drivers/driver/"), name="driver-list"),
    path("driver/", DriversListView.as_view(), name="driver-list"),
    path("register-drivers/", register_drivers, name="register-drivers"),
    path("", RedirectView.as_view(url="/skulbus_drivers/admin/"), name="home_url"),
]