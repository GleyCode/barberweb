"""
Nessa módulo, estão armazenadas as classes de view, mais específicamente 
classes de visualizações genéricas.

Cada classe trata de um CRUD específico, como criar um profissional, ler a 
tabela de profissional no banco de dados e gerar uma visualização em lista ou 
até mesmo, deletar um profissional do banco de dados.
"""


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Profissional


class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    """View para cadastrar um novo profissional no sistema."""
    model = Profissional
    template_name = "profissionais/cadastrar_profissional.html"
    fields = ['nome']
    success_url = reverse_lazy("profissionais:profissionais")
    raise_exception = True
    

class ProfissionalListView(LoginRequiredMixin, ListView):
    """View para apresentar os profissionais cadastrados em lista."""
    model = Profissional
    template_name = "profissionais/listagem_profissionais.html"
    context_object_name = "profissionais"
    ordering = ['nome']
    raise_exception = True
    

class ProfissionalDetailView(LoginRequiredMixin, DetailView):
    """View para detalhar um profissional mostrando seus dados."""
    model = Profissional
    template_name = "profissionais/detalhes_profissional.html"
    context_object_name = "profissional"
    raise_exception = True


class ProfissionalDeleteView(LoginRequiredMixin, DeleteView):
    """View para excluir um profissional do sistema."""
    model = Profissional
    template_name = "profissionais/deletar_profissional.html"
    context_object_name = "profissional"
    success_url = reverse_lazy("profissionais:profissionais")
    raise_exception = True
