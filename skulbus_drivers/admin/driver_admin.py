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
                    "middlename",
                    "lastname",
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
        "middlename",
        "lastname",
        "vehicle",
        "active",
    )

    search_fields = (
        "driving_licence",
        "firstname",
        "lastname",
        "vehicle",
        "active",
    )

    list_filter = (
        "driving_licence",
        "vehicle",
        "active",
    )


