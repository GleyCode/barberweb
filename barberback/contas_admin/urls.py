from django.urls import path
from django.contrib.auth import views

app_name = "contas_admin"
urlpatterns = [
    path('', 
         views.LoginView.as_view(template_name="contas_admin/login.html"), name="login"),
    path('logout/', 
         views.LogoutView.as_view(template_name="contas_admin/logged_out.html"), name="logout"),
]
