from django.views.generic.base import TemplateView
from django.apps import apps as django_apps

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_buses.models import Bus
from skulbus_drivers.models import Driver
from skulbus_parents.models import Parent
from skulbus_routes.models import Route, BusStop
from skulbus_schools.models import School
from skulbus_students.models import Student


class DashboardView(SkulBusLoginMixin, TemplateView):
    template_name = f"skulbus_dashboard/bootstrap/base.html"
    listboard_model = "skulbus_schools.school"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        students = Student.objects.all().count()
        parents = Parent.objects.all().count()
        buses = Bus.objects.all().count()
        schools = School.objects.all().count()
        routes = Route.objects.all().count()
        drivers = Driver.objects.all().count()
        bus_stops = BusStop.objects.all().count()
        context.update(
            students=students,
            parents=parents,
            buses=buses,
            schools=schools,
            routes=routes,
            drivers=drivers,
            bus_stops=bus_stops,
        )
        return context

    @property
    def listboard_model_cls(self):
        try:
            return django_apps.get_model(self.listboard_model)
        except (ValueError, AttributeError):
            return self.listboard_model

    @property
    def get_school_url(self):
        return self.listboard_model_cls().get_absolute_url()
