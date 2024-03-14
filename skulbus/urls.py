from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include("skulbus_dashboard.urls")),
    path("", include("skulbus_auth.urls"))
]
