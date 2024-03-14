from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_schools_admin = SkulbusAdminSite(name="skulbus_schools_admin", app_label=AppConfig.name)
