from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_routes_admin = SkulbusAdminSite(name="skulbus_routes_admin", app_label=AppConfig.name)
