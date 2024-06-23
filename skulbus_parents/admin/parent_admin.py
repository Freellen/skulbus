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
                    "user",
                    "firstname",
                    "lastname",
                    "address",
                    "phone",
                    "email",
                    "active",
                ),
            },
        ),
        audit_fieldset_tuple,
    )

    list_display = (
        "firstname",
        "lastname",
        "address",
        "phone",
        "username",
        "active",
    )

    search_fields = (
        "firstname",
        "lastname",
        "phone",
        "username",
    )

    list_filter = (
        "active",
    )
