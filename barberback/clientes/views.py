from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    """View Cadastra um novo cliente.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de cadastro de serviços. 
    Também utiliza a classe CreateView do Django para facilitar o processo de 
    criação de novos objetos do modelo Servico.
    
    Atributos:
        model: O modelo Cliente que será utilizado para criar novos clientes.
        template_name: O nome do template HTML que será renderizado para a
                       página de cadastro de clientes.
        fields: Uma lista dos campos do modelo Cliente que serão exibidos no
                formulário de cadastro.
        success_url: A URL para a qual o usuário será redirecionado após o
                     cadastro bem-sucedido de um cliente.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Cliente
    template_name = 'clientes/cadastrar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteListView(LoginRequiredMixin, ListView):
    """Lista todos os clientes cadastrados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de listagem de clientes. 
    Também utiliza a classe ListView do Django para facilitar o processo de 
    exibição de uma lista de objetos do modelo Cliente.
    
    Atributos:
        model: O modelo Cliente que será utilizado para listar os clientes.
        template_name: O nome do template HTML que será renderizado para a
                       página de listagem de clientes.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar a lista de clientes.
        ordering: A ordem em que os serviços serão exibidos na lista.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Cliente
    template_name = 'clientes/listagem_clientes.html'
    paginate_by = 10
    context_object_name = 'clientes'
    ordering = ['nome']
    raise_exception = True
    

class ClienteDetailView(LoginRequiredMixin, DetailView):
    """Apresenta os dados dos clientes.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de detalhes do cliente. 
    Também utiliza a classe DetailView do Django para facilitar o processo de 
    exibição dos detalhes de um objeto do modelo Cliente.
    
    Atributos:
        model: O modelo Cliente que será utilizado para exibir os detalhes do
               cliente.
        template_name: O nome do template HTML que será renderizado para a
                       página de detalhes do cliente.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o cliente.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Cliente
    template_name = 'clientes/detalhes_cliente.html'
    context_object_name = 'cliente'
    raise_exception = True
    

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    """Atualiza as informações dos clientes.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de atualização de clientes. 
    Também utiliza a classe UpdateView do Django para facilitar o processo de 
    atualização dos objetos do modelo Cliente.
    
    Atributos:
        model: O modelo Cliente que será utilizado para atualizar os clientes.
        template_name: O nome do template HTML que será renderizado para a
                       página de atualização de clientes.
        fields: Uma lista dos campos do modelo Cliente que serão exibidos no
                formulário de atualização.
        success_url: A URL para a qual o usuário será redirecionado após a
                     atualização bem-sucedida de um cliente.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Cliente
    template_name = 'clientes/atualizar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    """Deleta clientes do banco de dados.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de exclusão de clientes. 
    Também utiliza a classe DeleteView do Django para facilitar o processo de 
    exclusão dos objetos do modelo Cliente.
    
    Atributos:
        model: O modelo Cliente que será utilizado para deletar os clientes.
        template_name: O nome do template HTML que será renderizado para a
                       página de exclusão de clientes.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar o cliente.
        success_url: A URL para a qual o usuário será redirecionado após a
                     exclusão bem-sucedida de um cliente.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
    """
    
    model = Cliente
    template_name = 'clientes/deletar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True
