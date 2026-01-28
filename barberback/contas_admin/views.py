from django.contrib.auth.views import LoginView, LogoutView


class LoginAdminView(LoginView):
    """View realiza o processo de login.
     
    Utiliza a classe LoginView do Django que realiza todo o processo de 
    login por debaixo dos panos.
    
    Atributos:
        template_name: O nome do template HTML que será renderizado para a
                       página de login.
    """
    
    template_name = "contas_admin/login.html"
    

class LogoutAdminView(LogoutView):
    """View realiza o processo de logout.
     
    Utiliza a classe LogoutView do Django que realiza todo o processo de 
    logout por debaixo dos panos.
    
    Atributos:
        template_name: O nome do template HTML que será renderizado para a
                       página de logout.
    """
    
    template_name = "contas_admin/logged_out.html"
