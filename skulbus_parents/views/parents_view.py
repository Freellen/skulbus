from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView
from django.conf import settings

from skulbus_auth.view_mixins import SkulBusLoginMixin
from skulbus_dashboard.view_mixins import ListboardView
from skulbus_parents.models import Parent


class ParentsListView(SkulBusLoginMixin, ListboardView, ListView):
    template_name = f"skulbus_parents/bootstrap/parents.html"
    listboard_model = "skulbus_parents.parent"
    paginate_by = settings.SKULBUS_PAGINATION
    queryset = Parent.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            add_parent=self.get_parent_url,
            object_lists=self.queryset
        )
        return context

    @property
    def get_parent_url(self):
        return self.listboard_model_cls().get_absolute_url()


def register_parents(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        address = request.POST.get("address")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        next_url_name = request.POST.get("next_url_name")

        try:
            user = User.objects.create_user(username=username, password=password)
            user.save()

            parent, created = Parent.objects.get_or_create(
                user=user,
                username=username,
                firstname=firstname,
                lastname=lastname,
                address=address,
                phone=phone,
                email=email,
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
            [reverse(f'skulbus_parents:{next_url_name}'), notification])
    return redirect(url)
