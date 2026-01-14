from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Servico


class ServicoCreateView(LoginRequiredMixin, CreateView):
    """Cadastra um novo serviço."""
    model = Servico
    template_name = 'servicos/cadastrar_servico.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True


class ServicoListView(LoginRequiredMixin, ListView):
    """Lista todos os serviços cadastrados."""
    model = Servico
    template_name = 'servicos/listagem_servicos.html'
    context_object_name = 'servicos'
    ordering = ['nome']
    raise_exception = True
    

class ServicoDetailView(LoginRequiredMixin, DetailView):
    """Apresenta os dados dos servicos."""
    model = Servico
    template_name = 'servicos/detalhes_servico.html'
    context_object_name = 'servico'
    raise_exception = True
    

class ServicoUpdateView(LoginRequiredMixin, UpdateView):
    """Atualiza as informações dos serviços."""
    model = Servico
    template_name = 'servicos/atualizar_servico.html'
    fields = ['nome', 'descricao', 'preco']
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True


class ServicoDeleteView(LoginRequiredMixin, DeleteView):
    """Deleta serviços do banco de dados."""
    model = Servico
    template_name = 'servicos/deletar_servico.html'
    context_object_name = 'servico'
    success_url = reverse_lazy('servicos:servicos')
    raise_exception = True
