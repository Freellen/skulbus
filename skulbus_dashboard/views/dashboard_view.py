from django.views.generic.base import TemplateView

from skulbus_auth.view_mixins import SkulBusLoginMixin


class DashboardView(SkulBusLoginMixin, TemplateView):
    template_name = f"skulbus_dashboard/bootstrap/base.html"

    def get_context_data(self, **kwargs):
        menu_category = ''
        context = super().get_context_data(**kwargs)
        context.update()
        return context
