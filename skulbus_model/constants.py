from django.conf import settings
from django_audit_fields import AUDIT_MODEL_FIELDS

DEFAULT_BASE_FIELDS = list(
    set(AUDIT_MODEL_FIELDS + ["id", "device_created", "device_modified"])
)
REPORT_DATETIME_FIELD_NAME = getattr(
    settings, "EDC_MODEL_REPORT_DATETIME_FIELD_NAME", "report_datetime"
)
CLOSED = "closed"
OPEN = "open"
