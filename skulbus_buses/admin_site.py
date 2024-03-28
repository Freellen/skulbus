from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_buses_admin = SkulbusAdminSite(name="skulbus_buses_admin", app_label=AppConfig.name)
