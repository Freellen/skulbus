from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_drivers_admin
from ..models import Driver


@admin.register(Driver, site=skulbus_drivers_admin)
class DriverAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "firstname",
                    "lastname",
                    "username",
                    "password",
                    "phone",
                    "email",
                    "driving_licence",
                    "vehicle",
                    "active"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "driving_licence",
        "firstname",
        "lastname",
        "username",
        "phone",
        "email",
        "vehicle",
        "active",
    )

    search_fields = (
        "driving_licence",
        "username",
        "phone",
        "email",
        "vehicle",
        "active",
    )

    list_filter = (
        "vehicle",
        "active",
    )


