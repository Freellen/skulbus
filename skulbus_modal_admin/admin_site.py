from django.apps import apps as django_apps
from django.conf import settings
from django.contrib import admin
from django.contrib.admin import AdminSite as DjangoAdminSite
from django.contrib.sites.shortcuts import get_current_site

admin.site.enable_nav_sidebar = False


class SkulbusAdminSite(DjangoAdminSite):

    """
    Add to your project urls.py
        path("edcs_action_item/", edc_action_item.urls),

    -OR-
    To include this in the administration section set
    `AppConfig.include_in_administration_section = True`
    in your apps.py. (See also View `edcs_dashboard.administration.py`).

    If set to `include_in_administration_section=True`, add a local `urls.py`

        from django.urls.conf import path
        from django.views.generic import RedirectView

        app_name = "edcs_action_item"

        urlpatterns = [
            path("", RedirectView.as_view(url="admin/"), name="home_url"),
        ]

    and then add to your project urls.py

        path("edcs_action_item/admin/", edc_action_item_admin.urls),
        path("edcs_action_item/", include("edc_action_item.urls")),

    """

    # app_index_template = "edcs_model_admin/admin/app_index.html"
    login_template = f"skulbus_auth/bootstrap/login.html"
    logout_template = f"skulbus_auth/bootstrap/login.html"
    enable_nav_sidebar = False  # DJ 3.1
    final_catch_all_view = True  # DJ 3.2
    # site_url = "/administration/"

    def __init__(self, name="admin", app_label=None, keep_delete_action=None):
        self.app_label = app_label
        super().__init__(name)
        if not keep_delete_action:
            del self._actions["delete_selected"]



