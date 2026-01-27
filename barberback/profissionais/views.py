from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .models import Profissional


class ProfissionalCreateView(LoginRequiredMixin, CreateView):
    """View Cadastra um novo profissional.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de cadastro de profissionais. 
    Também utiliza a classe CreateView do Django para facilitar o processo de 
    criação de novos objetos do modelo Profissional.
    
    Atributos:
        model: O modelo Profissional que será utilizado para criar novos 
               profissionais.
        template_name: O nome do template HTML que será renderizado para a
                       página de cadastro de profissionais.
        fields: O campos do modelo Profissional que será exibido no formulário 
                de cadastro.
        success_url: A URL para a qual o usuário será redirecionado após o
                     cadastro bem-sucedido de um profissional.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Profissional
    template_name = "profissionais/cadastrar_profissional.html"
    fields = ['nome']
    success_url = reverse_lazy("profissionais:profissionais")
    raise_exception = True
    

class ProfissionalListView(LoginRequiredMixin, ListView):
    """Lista todos os profissionais cadastrados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de listagem de profissionais. 
    Também utiliza a classe ListView do Django para facilitar o processo de 
    exibição de uma lista de objetos do modelo Profissional.
    
    Atributos:
        model: O modelo Profissional que será utilizado para listar os 
               profissionais.
        template_name: O nome do template HTML que será renderizado para a
                       página de listagem de profissionais.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar a lista de profissionais.
        ordering: A ordem em que os profissionais serão exibidos na lista.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Profissional
    template_name = "profissionais/listagem_profissionais.html"
    context_object_name = "profissionais"
    ordering = ['nome']
    raise_exception = True
    

class ProfissionalDetailView(LoginRequiredMixin, DetailView):
    """Apresenta os dados dos profissionais.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de detalhes do profissional. 
    Também utiliza a classe DetailView do Django para facilitar o processo de 
    exibição dos detalhes de um objeto do modelo Profissional.
    
    Atributos:
        model: O modelo Profissional que será utilizado para exibir os detalhes 
               do profissional.
        template_name: O nome do template HTML que será renderizado para a
                       página de detalhes do profissional.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o profissional.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Profissional
    template_name = "profissionais/detalhes_profissional.html"
    context_object_name = "profissional"
    raise_exception = True


class ProfissionalDeleteView(LoginRequiredMixin, DeleteView):
    """Deleta profissionais do banco de dados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de exclusão de profissionais. 
    Também utiliza a classe DeleteView do Django para facilitar o processo de 
    exclusão dos objetos do modelo Profissional.
    
    Atributos:
        model: O modelo Profissional que será utilizado para deletar os 
               profissionais.
        template_name: O nome do template HTML que será renderizado para a
                       página de exclusão de profissionais.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o profissional.
        success_url: A URL para a qual o usuário será redirecionado após a
                     exclusão bem-sucedida de um profissional.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Profissional
    template_name = "profissionais/deletar_profissional.html"
    context_object_name = "profissional"
    success_url = reverse_lazy("profissionais:profissionais")
    raise_exception = True
