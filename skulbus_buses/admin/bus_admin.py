from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_buses_admin
from ..models import Bus


@admin.register(Bus, site=skulbus_buses_admin)
class BusAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "reg_number",
                    "model",
                    "seats",
                    "active"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "reg_number",
        "model",
        "seats",
        "active",
    )

    search_fields = (
        "reg_number",
        "model",
        "seats",
        "active",
    )

    list_filter = (
        "reg_number",
        "model",
        "seats",
        "active",
    )


