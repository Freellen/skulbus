from django.contrib.auth.models import User
from django.db import models
from skulbus_model import models as skulbus_models


class Parent(skulbus_models.BaseUuidModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    firstname = models.CharField(
        verbose_name="First Name",
        max_length=120,
    )
    lastname = models.CharField(
        verbose_name="Last Name",
        max_length=120,
    )
    address = models.CharField(
        verbose_name="Address",
        max_length=120,
    )
    username = models.CharField(
        verbose_name="Username",
        max_length=45,
        null=True,
    )
    password = models.CharField(
        verbose_name="Password",
        max_length=128,
    )
    phone = models.CharField(
        verbose_name="Phone Number",
        max_length=25,
        null=True
    )
    email = models.CharField(
        verbose_name="Email Address",
        max_length=80,
        null=True
    )

    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.firstname} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Parent"
        verbose_name_plural = "Parent"
