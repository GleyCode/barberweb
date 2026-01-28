from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', 
         admin.site.urls, name="admin"),
    path('', 
         include('contas_admin.urls')),
    path('painel/', 
         include('barberback_app.urls'), name="painel"),
    path('clientes/', 
         include('clientes.urls'), name="clientes"),
    path('servicos/', 
         include('servicos.urls'), name="servicos"),
    path('profissionais/', 
         include('profissionais.urls'), name="profissionais"),
    path('agendamentos/', 
         include('agendamentos.urls'), name="agendamentos")
]
