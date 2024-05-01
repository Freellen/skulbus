from django.db import models
from skulbus_model import models as skulbus_models
from skulbus_routes.models import Route


class Bus(skulbus_models.BaseUuidModel):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="bus_route",
        verbose_name="Route",
        null=True,
    )
    reg_number = models.CharField(
        verbose_name="Registration Number",
        max_length=20,
    )
    model = models.CharField(
        verbose_name="Model",
        max_length=140,
    )
    seats = models.IntegerField(
        verbose_name="Number of Seats",
    )
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.reg_number}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Buses"
        verbose_name_plural = "Buses"
