from django.urls import path

from . import views

app_name = "servicos"
urlpatterns = [
    path('', 
         views.ServicoListView.as_view(), name="servicos"), 
    path('cadastrar_servico/', 
         views.ServicoCreateView.as_view(), name='cadastrar_servico'),  
    path('atualizar_servico/<int:pk>/', 
         views.ServicoUpdateView.as_view(), name='atualizar_servico'), 
    path('detalhes_servico/<int:pk>/', 
         views.ServicoDetailView.as_view(), name='detalhes_servico'),  
    path('deletar_servico/<int:pk>/', 
         views.ServicoDeleteView.as_view(), name='deletar_servico'),
]