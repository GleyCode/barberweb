from django.urls import path

from . import views

app_name = "profissionais"
urlpatterns = [
    path('', 
         views.ProfissionalListView.as_view(), name="profissionais"),
    path('cadastrar_profissional', 
         views.ProfissionalCreateView.as_view(), name="cadastrar_profissional"),
    path('detalhes_profissional/<int:pk>/', 
         views.ProfissionalDetailView.as_view(), name="detalhes_profissional"),
    path('deletar_profissional/<int:pk>/', 
         views.ProfissionalDeleteView.as_view(), name="deletar_profissional")
]
