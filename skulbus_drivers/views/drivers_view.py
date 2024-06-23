from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.conf import settings

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_buses.models import Bus
from skulbus_dashboard.view_mixins import ListboardView
from skulbus_drivers.models import Driver
from skulbus_parents.models import Parent


class DriversListView(SkulBusLoginMixin, ListboardView, ListView):
    template_name = f"skulbus_drivers/bootstrap/drivers.html"
    listboard_model = "skulbus_drivers.driver"
    paginate_by = settings.SKULBUS_PAGINATION
    queryset = Driver.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vehicles = Bus.objects.all()
        context.update(
            vehicles=vehicles,
            add_driver=self.get_parent_url,
            object_lists=self.get_wrapped_queryset(self.queryset,
                                                   'skulbus_drivers:drivers-list')
        )
        return context

    @property
    def get_parent_url(self):
        return self.listboard_model_cls().get_absolute_url()


def register_drivers(request):
    if request.method == 'POST':
        vehicles = request.POST.get('vehicle')
        driving_licence = request.POST.get('driving_licence')
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        next_url_name = request.POST.get("next_url_name")

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            vehicle = Bus.objects.get(id=vehicles)

            parent, created = Driver.objects.get_or_create(
                user=user,
                vehicle=vehicle,
                username=username,
                firstname=firstname,
                lastname=lastname,
                phone=phone,
                email=email,
                driving_licence=driving_licence,
            )

            if created:
                res = 'success'
                message = 'Request submitted successfully'
            else:
                res = 'error'
                message = 'Error occurred while processing your request, please check your inputs and try again'
        except Exception as e:
            print(e)
            res = 'error'
            message = f'Error: {str(e)}'

        notification = res + '&message=' + message
        url = "?response=".join(
            [reverse(f'skulbus_drivers:{next_url_name}'), notification])
    return redirect(url)