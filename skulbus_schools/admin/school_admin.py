from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_schools_admin
from ..models import School


@admin.register(School, site=skulbus_schools_admin)
class SchoolAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "address",
                    "phone_number",
                    "latitude",
                    "longitude",
                    "active"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "name",
        "address",
        "phone_number",
        "longitude",
        "latitude",
        "active",
    )

    search_fields = (
        "name",
    )

    list_filter = (
        "name",
        "active",
    )
