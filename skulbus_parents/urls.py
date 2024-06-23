from django.urls.conf import path
from django.views.generic import RedirectView
from .admin_site import skulbus_parents_admin
from .views import ParentsListView
from .views.parents_view import register_parents

app_name = "skulbus_parents"

urlpatterns = [
    path("admin/", skulbus_parents_admin.urls),
    # path("parents/", RedirectView.as_view(
    #     url="/skulbus_parents/admin/skulbus_parents/parent/"), name="parents-list"),
    path("parents/", ParentsListView.as_view(), name="parents-list"),
    path("register-parent/", register_parents, name="register-parent"),
    path("", RedirectView.as_view(url="/skulbus_parents/admin/"), name="home_url"),
]