from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_schools_admin

app_name = "skulbus_students"

urlpatterns = [
    path("admin/", skulbus_schools_admin.urls),
    path("", RedirectView.as_view(url="/skulbus_students/admin/"), name="home_url"),
]