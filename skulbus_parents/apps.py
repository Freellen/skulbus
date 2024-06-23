from django.apps import AppConfig as DjangoAppConfig


class AppConfig(DjangoAppConfig):
    name = 'skulbus_parents'

    # def ready(self):
    #     import skulbus_parents.signals
