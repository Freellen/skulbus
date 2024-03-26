from django.db import models
from skulbus_model import models as skulbus_models


class Parent(skulbus_models.BaseUuidModel):
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
    address = models.CharField(
        verbose_name="School Address",
        max_length=120,
    )
    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=120,
    )
    email = models.CharField(
        verbose_name="Email Address",
        max_length=120,
    )
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.firstname} {self.middlename} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Parent"
        verbose_name_plural = "Parent"
