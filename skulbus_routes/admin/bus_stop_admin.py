from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_routes_admin
from ..models import Route, BusStop


@admin.register(BusStop, site=skulbus_routes_admin)
class BusStopAdmin(SimpleHistoryAdmin):
    # form = RouteForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "route",
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
        "route",
        "longitude",
        "latitude",
        "active"
    )

    search_fields = (
        "name",
        "route",
    )

    list_filter = (
        "name",
        "route",
    )
