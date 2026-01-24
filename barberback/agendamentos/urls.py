from django.urls import path

from . import views

app_name = "agendamentos"
urlpatterns = [
    # Ex.: dominio.com/agendamentos
    path('', 
         views.AgendamentoListView.as_view(), name="agendamentos"),
    # Ex.: dominio.com/agendamentos/criar_agendamento
    path('criar_agendamento/',
         views.AgendamentoCreateView.as_view(), name="criar_agendamento"),
    # Ex.: dominio.com/agendamentos/atualizar_agendamento/5
    path('atualizar_agendamento/<int:pk>/', 
         views.AgendamentoUpdateView.as_view(), name="atualizar_agendamento"),
    # Ex.: dominio.com/agendamentos/detalhes_agendamento/5
    path('detalhes_agendamento/<int:pk>/', 
         views.AgendamentoDetailView.as_view(), name="detalhes_agendamento"),
    # Ex.: dominio.com/agendamentos/excluir_agendamento/5
    path('deletar_agendamento/<int:pk>/', 
         views.AgendamentoDeleteView.as_view(), name="deletar_agendamento"),
]
