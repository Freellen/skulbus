import getpass
from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag(
    f"skulbus_dashboard/bootstrap/menu/mobile-menu.html",
    takes_context=True,
)
def mobile_menu(context):
    title = None
    return dict(
        title=title,
    )


@register.inclusion_tag(
    f"skulbus_dashboard/bootstrap/menu/top-bar-menu.html",
    takes_context=True,
)
def top_bar_menu(context, adm=False):
    title = None
    return dict(
        title=title,
        frdrck=adm,
        username=context.get('user'),
    )


@register.inclusion_tag(
    f"skulbus_dashboard/bootstrap/menu/main-menu.html",
    takes_context=True,
)
def main_menu(context):

    return dict(

    )


@register.simple_tag(takes_context=True)
def get_url_name(context, url):
    url_name = url.split('/')
    return url_name[-2]
