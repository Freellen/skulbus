from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from skulbus_model import models as skulbus_models
from skulbus_students.choices import TRIP_STATUS


class StudentTrip(skulbus_models.BaseUuidModel):
    parent = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    firstname = models.CharField(
        verbose_name="First Name",
        max_length=120,
    )
    middlename = models.CharField(
        verbose_name="Middle Name",
        max_length=120,
    )
    lastname = models.CharField(
        verbose_name="Last Name",
        max_length=120,
    )
    verification = models.CharField(
        verbose_name="Verification Code",
        max_length=120,
    )
    bus_stop = models.CharField(
        verbose_name="Bus Stop",
        max_length=120,
        null=True,
    )
    latitude = models.DecimalField(
        verbose_name="Latitude",
        max_digits=16,
        decimal_places=8
    )
    longitude = models.DecimalField(
        verbose_name="Longitude",
        max_digits=16,
        decimal_places=8
    )
    status = models.CharField(
        verbose_name="Status",
        max_length=16,
        choices=TRIP_STATUS,
    )
    timestamp = models.DateTimeField(
        verbose_name="Timestamp",
        default=timezone.now,
    )

    def __str__(self):
        return f'{self.firstname} {self.middlename} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Student Trip"
        verbose_name_plural = "Student Trip"
