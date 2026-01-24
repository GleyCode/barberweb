from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Cliente


class ClienteCreateView(LoginRequiredMixin, CreateView):
    """View para cadastro de novo cliente no sistema."""
    model = Cliente
    template_name = 'clientes/cadastrar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteListView(LoginRequiredMixin, ListView):
    """View para criar uma apresentação em lista dos clientes cadastrados."""
    model = Cliente
    template_name = 'clientes/listagem_clientes.html'
    paginate_by = 10
    context_object_name = 'clientes'
    ordering = ['nome']
    raise_exception = True
    

class ClienteDetailView(LoginRequiredMixin, DetailView):
    """View para detalhar um cliente mostrando seus dados."""
    model = Cliente
    template_name = 'clientes/detalhes_cliente.html'
    context_object_name = 'cliente'
    raise_exception = True
    

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    """View para atualizar os dados de um cliente."""
    model = Cliente
    template_name = 'clientes/atualizar_cliente.html'
    fields = ['nome', 'telefone', 'email']
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True


class ClienteDeleteView(LoginRequiredMixin, DeleteView):
    """View para excluir um cliente do sistema."""
    model = Cliente
    template_name = 'clientes/deletar_cliente.html'
    context_object_name = 'cliente'
    success_url = reverse_lazy('clientes:clientes')
    raise_exception = True
