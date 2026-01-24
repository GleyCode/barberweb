from django.urls import path

from . import views

app_name = "servicos"
urlpatterns = [
    # Ex.: dominio.com/servicos/
    path('', views.ServicoListView.as_view(), name="servicos"), 
    # Ex.: dominio.com/servicos/cadastrar_servico/ 
    path('cadastrar_servico/', views.ServicoCreateView.as_view(), name='cadastrar_servico'),  
    # Ex.: dominio.com/servicos/atualizar_servico/1/
    path('atualizar_servico/<int:pk>/', views.ServicoUpdateView.as_view(), name='atualizar_servico'), 
    # Ex.: dominio.com/servicos/detalhes_servico/1/
    path('detalhes_servico/<int:pk>/', views.ServicoDetailView.as_view(), name='detalhes_servico'),  
    # Ex.: dominio.com/servicos/deletar_servico/1/
    path('deletar_servico/<int:pk>/', views.ServicoDeleteView.as_view(), name='deletar_servico'),
]