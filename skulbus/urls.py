from django.contrib import admin
from django.urls import path, include
from edc_utils.paths_for_urlpatterns import paths_for_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include("skulbus_dashboard.urls")),
    *paths_for_urlpatterns("skulbus_schools"),
    *paths_for_urlpatterns("skulbus_students"),
    *paths_for_urlpatterns("skulbus_parents"),
    path("", include("skulbus_auth.urls"))
]
