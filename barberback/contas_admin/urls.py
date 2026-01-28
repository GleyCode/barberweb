from django.urls import path

from . import views

app_name = "contas_admin"
urlpatterns = [
    path('', 
         views.LoginAdminView.as_view(), name="login"),
    path('logout/', 
         views.LogoutAdminView.as_view(), name="logout"),
]
