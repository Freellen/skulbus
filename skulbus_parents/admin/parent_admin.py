from django.contrib import admin
from django_audit_fields import audit_fieldset_tuple
from simple_history.admin import SimpleHistoryAdmin

from ..admin_site import skulbus_parents_admin
from ..models import Parent


@admin.register(Parent, site=skulbus_parents_admin)
class ParentAdmin(SimpleHistoryAdmin):
    # form = SchoolForm

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "firstname",
                    "middlename",
                    "lastname",
                    "address",
                    "phone",
                    "email",
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
        "address",
        "phone",
        "email",
        "active",
    )

    search_fields = (
        "firstname",
        "lastname",
        "phone",
        "email",
    )

    list_filter = (
        "phone",
        "email",
    )
