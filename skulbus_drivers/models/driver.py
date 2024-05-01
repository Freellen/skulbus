from django.db import models

from skulbus_buses.models import Bus
from skulbus_model import models as skulbus_models


class Driver(skulbus_models.BaseUuidModel):
    firstname = models.CharField(
        verbose_name="First Name",
        max_length=120,
    )
    middlename = models.CharField(
        verbose_name="Middle Name",
        max_length=120,
        blank=True,
        null=True,
    )
    lastname = models.CharField(
        verbose_name="Last Name",
        max_length=120,
    )
    driving_licence = models.CharField(
        verbose_name="Driving licence Number",
        max_length=120,
    )
    vehicle = models.ForeignKey(
        Bus,
        on_delete=models.CASCADE,
        related_name="driver_bus",
        verbose_name="Vehicle",
        null=True,
    )
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.driving_licence} {self.firstname} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Driver"
        verbose_name_plural = "Driver"
