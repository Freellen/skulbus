from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_students_admin
from ..models import Student


@admin.register(Student, site=skulbus_students_admin)
class StudentAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "firstname",
                    "middlename",
                    "lastname",
                    "parent",
                    "school",
                    "active"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "firstname",
        "middlename",
        "lastname",
        "parent",
        "school",
        "active",
    )

    search_fields = (
        "firstname",
        "lastname",
        "parent",
        "school",
    )

    list_filter = (
        "school",
    )

