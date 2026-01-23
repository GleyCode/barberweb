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
    """
    A função dessa view é cadastrar um novo profissional no sistema.
    """
    model = Profissional
    template_name = "profissionais/cadastrar_profissional.html"
    fields = ['nome']
    success_url = reverse_lazy("profissionais:profissional")
    raise_exception = True
    

class ProfissionalListView(LoginRequiredMixin, ListView):
    """
    A função dessa view é criar uma apresentação em lista dos profissionais 
    cadastrados.
    """
    model = Profissional
    template_name = "profissionais/listagem_profissionais.html"
    context_object_name = "profissionais"
    ordering = ['nome']
    raise_exception = True
    

class ProfissionalDetailView(LoginRequiredMixin, DetailView):
    """
    A função dessa view é detalhar um profissional mostrando seus dados.
    """
    model = Profissional
    template_name = "profissionais/detalhes_profissional.html"
    context_object_name = "profissional"
    raise_exception = True


class ProfissionalDeleteView(LoginRequiredMixin, DeleteView):
    """
    A função dessa view é excluir um profissional do sistema.
    """
    model = Profissional
    template_name = "profissionais/deletar_profissional.html"
    context_object_name = "profissional"
    raise_exception = True
