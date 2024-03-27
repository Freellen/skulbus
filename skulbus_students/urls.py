from django.urls.conf import path
from django.contrib import admin
from django.views.generic import RedirectView
from .admin_site import skulbus_students_admin
from .views import StudentsListView

app_name = "skulbus_students"
admin.site.site_header = 'SKULBUS Administration'

urlpatterns = [
    path("admin/", skulbus_students_admin.urls),
    path("student/", RedirectView.as_view(
        url="/skulbus_students/admin/skulbus_students/student"), name="students-list"),
    path("", RedirectView.as_view(url="/skulbus_students/admin/"), name="home_url"),
]