"""
Nessa módulo, estão armazenadas as classes de view, mais específicamente 
classes de visualizações genéricas.

Cada classe trata de um CRUD específico, como criar um profissional, ler a 
tabela de profissional no banco de dados e gerar uma visualização em lista ou 
até mesmo, deletar um profissional do banco de dados.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView

from .models import Profissional


class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    """
    Essa classe é responsável por receber a requisição do cliente e tratar, 
    passando os dados de contexto para o template para renderização.
    
    Como Django já possui uma implementação que atenda a essa tarefa, decidi 
    usar (View Genérica) para isso.
    
    A função dessa view é cadastrar um novo profissional no sistema.
    """
    model = Profissional
    template_name = "profissionais/cadastrar_profissional.html"
    raise_exception = True
    

class ProfissionalListView(LoginRequiredMixin, ListView):
    """
    Essa classe é responsável por receber a requisição do cliente e tratar, 
    passando os dados de contexto para o template para renderização.
    
    Como Django já possui uma implementação que atenda a essa tarefa, decidi 
    usar (View Genérica) para isso.
    
    A função dessa view é criar uma apresentação em lista dos profissionais 
    cadastrados.
    """
    model = Profissional
    template_name = "profissionais/listagem_profissionais.html"
    raise_exception = True
    

class ProfissionalDetailView(LoginRequiredMixin, DetailView):
    """
    Essa classe é responsável por receber a requisição do cliente e tratar, 
    passando os dados de contexto para o template para renderização.
    
    Como Django já possui uma implementação que atenda a essa tarefa, decidi 
    usar (View Genérica) para isso.
    
    A função dessa view é detalhar o profissional mostrando seus dados.
    """
    model = Profissional
    template_name = "profissionais/detalhes_profissional.html"
    raise_exception = True


class ProfissionalDeleteView(LoginRequiredMixin, DeleteView):
    """
    Essa classe é responsável por receber a requisição do cliente e tratar, 
    passando os dados de contexto para o template para renderização.
    
    Como Django já possui uma implementação que atenda a essa tarefa, decidi 
    usar (View Genérica) para isso.
    
    A função dessa view é excluir um profissional do sistema.
    """
    model = Profissional
    template_name = "profissionais/deletar_profissional.html"
    raise_exception = True
    