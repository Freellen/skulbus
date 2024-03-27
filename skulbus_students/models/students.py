from django.db import models
from skulbus_model import models as skulbus_models
from skulbus_parents.models import Parent
from skulbus_schools.models import School


class Student(skulbus_models.BaseUuidModel):
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
    parent = models.ForeignKey(
        Parent,
        on_delete=models.CASCADE,
        related_name="child",
        verbose_name="Parent",
    )
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
        related_name="student",
        verbose_name="School",
    )
    active = models.BooleanField(
        verbose_name="Active",
        default=True,
    )

    def __str__(self):
        return f'{self.firstname} {self.middlename} {self.lastname}'

    class Meta(skulbus_models.BaseUuidModel.Meta):
        verbose_name = "Student"
        verbose_name_plural = "Student"
