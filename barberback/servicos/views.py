from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Servico


class ServicoCreateView(LoginRequiredMixin, CreateView):
    """View Cadastra um novo serviço.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de cadastro de serviços. 
    Também utiliza a classe CreateView do Django para facilitar o processo de 
    criação de novos objetos do modelo Servico.
    
    Atributos:
        model: O modelo Servico que será utilizado para criar novos serviços.
        template_name: O nome do template HTML que será renderizado para a
                       página de cadastro de serviços.
        fields: Uma lista dos campos do modelo Servico que serão exibidos no
                formulário de cadastro.
        success_url: A URL para a qual o usuário será redirecionado após o
                     cadastro bem-sucedido de um serviço.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Servico
    template_name = 'servicos/cadastrar_servico.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True


class ServicoListView(LoginRequiredMixin, ListView):
    """Lista todos os serviços cadastrados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de listagem de serviços. 
    Também utiliza a classe ListView do Django para facilitar o processo de 
    exibição de uma lista de objetos do modelo Servico.
    
    Atributos:
        model: O modelo Servico que será utilizado para listar os serviços.
        template_name: O nome do template HTML que será renderizado para a
                       página de listagem de serviços.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar a lista de serviços.
        ordering: A ordem em que os serviços serão exibidos na lista.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Servico
    template_name = 'servicos/listagem_servicos.html'
    context_object_name = 'servicos'
    ordering = ['nome']
    raise_exception = True
    

class ServicoDetailView(LoginRequiredMixin, DetailView):
    """Apresenta os dados dos servicos.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de detalhes do serviço. 
    Também utiliza a classe DetailView do Django para facilitar o processo de 
    exibição dos detalhes de um objeto do modelo Servico.
    
    Atributos:
        model: O modelo Servico que será utilizado para exibir os detalhes do
               serviço.
        template_name: O nome do template HTML que será renderizado para a
                       página de detalhes do serviço.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o serviço.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Servico
    template_name = 'servicos/detalhes_servico.html'
    context_object_name = 'servico'
    raise_exception = True
    

class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    """Atualiza as informações dos serviços.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de atualização de serviços. 
    Também utiliza a classe UpdateView do Django para facilitar o processo de 
    atualização dos objetos do modelo Servico.
    
    Atributos:
        model: O modelo Servico que será utilizado para atualizar os serviços.
        template_name: O nome do template HTML que será renderizado para a
                       página de atualização de serviços.
        fields: Uma lista dos campos do modelo Servico que serão exibidos no
                formulário de atualização.
        success_url: A URL para a qual o usuário será redirecionado após a
                     atualização bem-sucedida de um serviço.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Servico
    template_name = 'servicos/atualizar_servico.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    """Deleta serviços do banco de dados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de exclusão de serviços. 
    Também utiliza a classe DeleteView do Django para facilitar o processo de 
    exclusão dos objetos do modelo Servico.
    
    Atributos:
        model: O modelo Servico que será utilizado para deletar os serviços.
        template_name: O nome do template HTML que será renderizado para a
                       página de exclusão de serviços.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o serviço.
        success_url: A URL para a qual o usuário será redirecionado após a
                     exclusão bem-sucedida de um serviço.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Servico
    template_name = 'servicos/deletar_servico.html'
    context_object_name = 'servico'
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True
