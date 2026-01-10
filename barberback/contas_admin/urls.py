from django.urls import path

from . import views

app_name = "contas_admin"
urlpatterns = [
    # Ex: dominio.com
    path('', views.LoginAdminView.as_view(), name="login"),
    # Ex.: dominio.com/logout/
    path('logout/', views.LogoutAdminView.as_view(), name="logout"),
]
