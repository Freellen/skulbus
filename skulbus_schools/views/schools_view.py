from django.views.generic import ListView
from django.conf import settings

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_dashboard.view_mixins import ListboardView
from skulbus_schools.models import School


class SchoolsListView(SkulBusLoginMixin, ListboardView, ListView):
    template_name = f"skulbus_schools/bootstrap/schools.html"
    # listboard_url = "subject_listboard_url"
    listboard_model = "skulbus_schools.school"
    paginate_by = settings.SKULBUS_PAGINATION
    queryset = School.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_wrapped_queryset(self.queryset))
        context.update(
            add_school=self.get_school_url,
            object_lists=self.get_wrapped_queryset(self.queryset)
        )
        return context

    @property
    def get_school_url(self):
        return self.listboard_model_cls().get_absolute_url()