from django.db import models
from skulbus_model import models as skulbus_models


class School(skulbus_models.BaseUuidModel):
    name = models.CharField(
        verbose_name="School Name",
        max_length=120,
    )
    address = models.CharField(
        verbose_name="School Address",
        max_length=120,
    )
    phone_number = models.CharField(
        verbose_name="School Phone Number",
        max_length=120,
    )
    longitude = models.DecimalField(
        verbose_name="Longitude",
        max_digits=16,
        decimal_places=6
    )
    latitude = models.DecimalField(
        verbose_name="Latitude",
        max_digits=16,
        decimal_places=6
    )

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "School"
        verbose_name_plural = "School"
