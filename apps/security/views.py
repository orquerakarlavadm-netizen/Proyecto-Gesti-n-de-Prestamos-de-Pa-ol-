from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView


class LoginView(DjangoLoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    next_page = '/inicio/'