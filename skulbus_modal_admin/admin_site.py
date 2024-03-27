from django.contrib import admin
from django.contrib.admin import AdminSite as DjangoAdminSite

admin.site.enable_nav_sidebar = False


class SkulbusAdminSite(DjangoAdminSite):
    login_template = f"skulbus_auth/bootstrap/login.html"
    logout_template = f"skulbus_auth/bootstrap/login.html"
    enable_nav_sidebar = False  # DJ 3.1
    final_catch_all_view = True  # DJ 3.2
    site_header = "SKULBUS Administration"

    def __init__(self, name="admin", app_label=None, keep_delete_action=None):
        self.app_label = app_label
        super().__init__(name)
        if not keep_delete_action:
            del self._actions["delete_selected"]



