from django.apps import apps as django_apps
from django.urls import reverse
from django.utils.translation import gettext as _


class ListboardViewError(Exception):
    pass


class BaseListboardView:
    context_object_name = "results"
    empty_queryset_message = _("Nothing to display.")
    listboard_url = None  # an existing key in request.context_data
    listboard_back_url = None
    listboard_dashboard = None
    subjectvisit_model = None

    listboard_model = None  # label_lower model name or model class
    model_consent = None
    listboard_model_manager_name = "_default_manager"
    subject_list_dashboard = None
    paginator_url = None

    model_wrapper_cls = None
    ordering = "-created"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    @property
    def listboard_model_cls(self):
        """Returns the listboard's model class.

        Accepts `listboard_model` as a model class or label_lower.
        """
        if not self.listboard_model:
            raise ListboardViewError(
                f"Listboard model not declared. Got None. See {repr(self)}"
            )
        try:
            return django_apps.get_model(self.listboard_model)
        except (ValueError, AttributeError):
            return self.listboard_model

    def get_wrapped_queryset(self, queryset):
        wrapped_objs = []
        for obj_qry in queryset:
            obj = self.get_model_dict(obj_qry)

            obj['href'] = self.listboard_model_cls().admin_url(obj_qry.id)
            wrapped_objs.append(obj)
        return wrapped_objs

    @staticmethod
    def get_model_dict(queryset):
        return queryset.__dict__


class ListboardView(BaseListboardView):
    urlconfig_getattr = "listboard_urls"

    @classmethod
    def get_urlname(cls):
        return cls.listboard_url


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)
