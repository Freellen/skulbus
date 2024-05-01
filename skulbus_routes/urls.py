from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_routes_admin

app_name = "skulbus_routes"

urlpatterns = [
    path("admin/", skulbus_routes_admin.urls),
    path("routes/", RedirectView.as_view(
        url="/skulbus_routes/admin/skulbus_routes/route/"), name="route-list"),
    path("bus-stop/", RedirectView.as_view(
        url="/skulbus_routes/admin/skulbus_routes/busstop/"), name="bus-stop-list"),
    path("", RedirectView.as_view(url="/skulbus_routes/admin/"), name="home_url"),
]