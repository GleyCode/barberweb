from django.urls import path

from . import views

app_name = "barberback_app"
urlpatterns = [
    # Ex: dominio.com/painel/
    path('', views.IndexView.as_view(), name="index"),
]