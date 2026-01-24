from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ex.: dominio.com/admin
    path('admin/', admin.site.urls, name="admin"),
    # Ex.: dominio.com
    path('', include('contas_admin.urls')),
    # Ex.: dominio.com/painel
    path('painel/', include('barberback_app.urls'), name="painel"),
    # Ex.: dominio.com/clientes
    path('clientes/', include('clientes.urls'), name="clientes"),
    # Ex.: dominio.com/servicos
    path('servicos/', include('servicos.urls'), name="servicos"),
    # Ex.: dominio.com/profissionais
    path('profissionais/', include('profissionais.urls'), name="profissionais"),
    # Ex.: dominio.com/agendamentos
    path('agendamentos/', include('agendamentos.urls'), name="agendamentos")
]
