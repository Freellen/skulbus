from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_parents_admin = SkulbusAdminSite(name="skulbus_parents_admin", app_label=AppConfig.name)
