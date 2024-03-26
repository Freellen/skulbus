from skulbus_modal_admin.admin_site import SkulbusAdminSite

from .apps import AppConfig

skulbus_students_admin = SkulbusAdminSite(name="skulbus_students_admin", app_label=AppConfig.name)
