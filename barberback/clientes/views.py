from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    """Cadastra um novo cliente."""
    model = Cliente
    template_name = 'clientes/cadastrar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteListView(LoginRequiredMixin, ListView):
    """Lista todos os clientes cadastrados."""
    model = Cliente
    template_name = 'clientes/listagem_clientes.html'
    paginate_by = 10
    context_object_name = 'clientes'
    ordering = ['nome']
    raise_exception = True
    

class ClienteDetailView(LoginRequiredMixin, DetailView):
    """Apresenta os dados dos clientes."""
    model = Cliente
    template_name = 'clientes/detalhes_cliente.html'
    context_object_name = 'cliente'
    raise_exception = True
    

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    """Atualiza os dados dos clientes."""
    model = Cliente
    template_name = 'clientes/atualizar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    """Deleta clientes do banco de dados."""
    model = Cliente
    template_name = 'clientes/deletar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True
