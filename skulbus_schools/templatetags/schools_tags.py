from django import template

register = template.Library()

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
