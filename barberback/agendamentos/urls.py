from django.urls import path

from . import views

app_name = "agendamentos"
urlpatterns = [
    path('', 
         views.AgendamentoListView.as_view(), name="agendamentos"),
    path('criar_agendamento/',
         views.AgendamentoCreateView.as_view(), name="criar_agendamento"),
    path('atualizar_agendamento/<int:pk>/', 
         views.AgendamentoUpdateView.as_view(), name="atualizar_agendamento"),
    path('detalhes_agendamento/<int:pk>/', 
         views.AgendamentoDetailView.as_view(), name="detalhes_agendamento"),
    path('deletar_agendamento/<int:pk>/', 
         views.AgendamentoDeleteView.as_view(), name="deletar_agendamento"),
]
