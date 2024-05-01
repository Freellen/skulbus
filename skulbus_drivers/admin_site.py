from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_drivers_admin = SkulbusAdminSite(name="skulbus_drivers_admin", app_label=AppConfig.name)
