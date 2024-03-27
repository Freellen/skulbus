from django.views.generic import ListView
from django.conf import settings

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_dashboard.view_mixins import ListboardView
from skulbus_parents.models import Parent


class ParentsListView(SkulBusLoginMixin, ListboardView, ListView):
    template_name = f"skulbus_parents/bootstrap/parents.html"
    listboard_model = "skulbus_parents.parent"
    paginate_by = settings.SKULBUS_PAGINATION
    queryset = Parent.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            add_parent=self.get_parent_url,
            object_lists=self.get_wrapped_queryset(self.queryset, 'skulbus_parents:parents-list')
        )
        return context

    @property
    def get_parent_url(self):
        return self.listboard_model_cls().get_absolute_url()