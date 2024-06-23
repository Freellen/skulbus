from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_students_admin
from ..models import StudentTrip


@admin.register(StudentTrip, site=skulbus_students_admin)
class StudentTripAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "firstname",
                    "middlename",
                    "lastname",
                    "verification",
                    "latitude",
                    "longitude",
                    "status",
                    "timestamp",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "firstname",
        "middlename",
        "lastname",
        "verification",
        "latitude",
        "longitude",
        "status",
        "timestamp",
    )

    search_fields = (
        "firstname",
        "lastname",
    )

    list_filter = (
        "status",
    )

