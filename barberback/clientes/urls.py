from django.urls import path

from . import views

app_name = "clientes"

urlpatterns = [
    # Ex: dominio.com/clientes/
    path('', views.ClienteListView.as_view(), name="clientes"),
    
    # Ex.: dominio.com/clientes/cadastrar_cliente/
    path('cadastrar_cliente/', views.ClienteCreateView.as_view(), name='cadastrar_cliente'),
    
    # Ex.: dominio.com/clientes/atualizar_cliente/5/
    path('atualizar_cliente/<int:pk>/', views.ClienteUpdateView.as_view(), name='atualizar_cliente'),
    
    # Ex.: dominio.com/clientes/detalhes_cliente/5/
    path('detalhes_cliente/<int:pk>/', views.ClienteDetailView.as_view(), name='detalhes_cliente'),
    
    # Ex.: dominio.com/clientes/deletar_cliente/5/
    path('deletar_cliente/<int:pk>/', views.ClienteDeleteView.as_view(), name='deletar_cliente'),
]
