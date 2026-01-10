from django.contrib.auth.views import LoginView, LogoutView


class LoginAdminView(LoginView):
    """View genérica para login de administradores."""
    template_name = "contas_admin/login.html"
    

class LogoutAdminView(LogoutView):
    """View genérica para logout de administradores."""
    template_name = "contas_admin/logged_out.html"
