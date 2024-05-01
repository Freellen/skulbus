from django.db import models
from skulbus_model import models as skulbus_models
from skulbus_routes.models import Route


class BusStop(skulbus_models.BaseUuidModel):
    name = models.CharField(
        verbose_name="Name",
        max_length=120,
    )
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name="bus_stop_route",
        verbose_name="Route",
        null=True,
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
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return self.name

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Bus Stop"
        verbose_name_plural = "Bus Stop"
