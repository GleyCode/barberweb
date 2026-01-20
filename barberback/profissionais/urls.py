from django.urls import path

from . import views

app_name = "profissionais"
urlpatterns = [
    # Ex: dominio.com/profissionais/
    path('', 
         views.ProfissionalListView.as_view(), name="profissional"),
    # Ex.: dominio.com/profissionais/cadastrar_profissional/
    path('cadastrar_profissional', 
         views.ProfissionalCreateView.as_view(), name="cadastrar_profissional"),
    # Ex.: dominio.com/profissionais/detalhes_profissional/
    path('detalhes_profissional/', 
         views.ProfissionalDetailView.as_view(), name="detalhes_profissional"),
    # Ex.: dominio.com/profissionais/deletar_profissional/
    path('deletar_profissional', 
         views.ProfissionalDeleteView.as_view(), name="deletar_profissional")
]
