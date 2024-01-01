from django.urls import path

from skulbus_auth.views import LoginView, LogoutView

app_name = "skulbus_auth"

urlpatterns = [
    path('', LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path('logout/', LogoutView.as_view(template_name="skulbus_auth/bootstrap/login.html"),
         name="logout",),
]
