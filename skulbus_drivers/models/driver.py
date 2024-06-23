from django.contrib.auth.models import User
from django.db import models

from skulbus_buses.models import Bus
from skulbus_model import models as skulbus_models


class Driver(skulbus_models.BaseUuidModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    firstname = models.CharField(
        verbose_name="First Name",
        max_length=120,
    )
    lastname = models.CharField(
        verbose_name="Last Name",
        max_length=120,
    )
    username = models.CharField(
        verbose_name="Username",
        max_length=45,
        unique=True,
        null=True
    )
    password = models.CharField(
        verbose_name="Password",
        max_length=128
    )
    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=45,
        unique=True,
        null=True
    )
    email = models.EmailField(
        verbose_name="Email Address",
        unique=True,
        null=True,
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
        return f'{self.firstname} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Driver"
        verbose_name_plural = "Driver"
