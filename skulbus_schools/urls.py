from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_schools_admin
from .views import SchoolsListView

app_name = "skulbus_schools"

urlpatterns = [
    path("admin/", skulbus_schools_admin.urls),
    path("schools/", SchoolsListView.as_view(), name="schools-list"),
    path("", RedirectView.as_view(url="/skulbus_schools/admin/"), name="home_url"),
]