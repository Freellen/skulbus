from django import template

register = template.Library()


@register.inclusion_tag(
    f"skulbus_parents/bootstrap/buttons/edit_school_info.html",
    takes_context=True,
)
def edit_parent_info(context, obj):
    return dict(

    )


@register.simple_tag(takes_context=True)
def get_url_name(context, url):
    url_name = url.split('/')
    return url_name[-2]
