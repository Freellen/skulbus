from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class SkulBusLoginMixin:
    @method_decorator(login_required(login_url='skulbus_auth:login'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)