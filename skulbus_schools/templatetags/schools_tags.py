import getpass
from django import template
from django.conf import settings
from django.urls import reverse
from django.apps import apps as django_apps

from skulbus_schools.models import School

register = template.Library()

school_model = "skulbus_schools.school"


def school_edit_url(obj):
    return django_apps.get_model(school_model).get_absolute_url()


@register.inclusion_tag(
    f"skulbus_schools/bootstrap/buttons/edit_school_info.html",
    takes_context=True,
)
def edit_school_info(context, obj):
    return dict(
        # href=reverse(school_edit_url)
    )


@register.simple_tag(takes_context=True)
def get_url_name(context, url):
    url_name = url.split('/')
    return url_name[-2]
