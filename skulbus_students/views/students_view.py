from django.views.generic import ListView
from django.conf import settings

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_dashboard.view_mixins import ListboardView
from skulbus_students.models import Student


class StudentsListView(SkulBusLoginMixin, ListboardView, ListView):
    template_name = f"skulbus_students/bootstrap/students.html"
    listboard_model = "skulbus_students.student"
    paginate_by = settings.SKULBUS_PAGINATION
    queryset = Student.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.get_wrapped_queryset(self.queryset, 'skulbus_students:students-list'))
        context.update(
            add_student=self.get_student_url,
            object_lists=self.get_wrapped_queryset(self.queryset,
                                                   'skulbus_students:students-list')
        )
        return context

    @property
    def get_student_url(self):
        return self.listboard_model_cls().get_absolute_url()