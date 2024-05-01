from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_routes_admin
from ..models import Route


@admin.register(Route, site=skulbus_routes_admin)
class RouteAdmin(SimpleHistoryAdmin):
    # form = RouteForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "starting_point",
                    "end_point",
                    "active"
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "name",
        "starting_point",
        "end_point",
        "active"
    )

    search_fields = (
        "name",
        "starting_point",
        "end_point",
    )

    list_filter = (
        "name",
        "starting_point",
        "end_point"
    )
