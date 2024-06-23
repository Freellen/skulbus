from django.db import models
from skulbus_model import models as skulbus_models


class Route(skulbus_models.BaseUuidModel):
    name = models.CharField(
        verbose_name="Name",
        max_length=120,
    )
    starting_point = models.CharField(
        verbose_name="Start At",
        max_length=120,
    )
    start_latitude = models.DecimalField(
        verbose_name="Route Start Latitude",
        max_digits=16,
        decimal_places=6,
        null=True,
    )
    start_longitude = models.DecimalField(
        verbose_name="Route Start Longitude",
        max_digits=16,
        decimal_places=6,
        null=True,
    )
    end_point = models.CharField(
        verbose_name="End At",
        max_length=120,
    )
    end_latitude = models.DecimalField(
        verbose_name="Route End Latitude",
        max_digits=16,
        decimal_places=6,
        null=True,
    )
    end_longitude = models.DecimalField(
        verbose_name="Route End Longitude",
        max_digits=16,
        decimal_places=6,
        null=True,
    )
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Route"
        verbose_name_plural = "Route"
