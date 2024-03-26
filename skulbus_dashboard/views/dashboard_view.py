from django.views.generic.base import TemplateView
from django.apps import apps as django_apps

from skulbus_auth.view_mixins import SkulBusLoginMixin


class DashboardView(SkulBusLoginMixin, TemplateView):
    template_name = f"skulbus_dashboard/bootstrap/base.html"
    listboard_model = "skulbus_schools.school"

    def get_context_data(self, **kwargs):
        print(self.get_school_url)
        context = super().get_context_data(**kwargs)
        context.update()
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
