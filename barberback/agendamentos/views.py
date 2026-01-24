from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Agendamento


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    """View para criar um novo agendamento."""
    model = Agendamento
    template_name = 'agendamentos/criar_agendamento.html'
    fields = ['cliente', 'profissional', 'servico', 'data_hora']
    success_url = reverse_lazy('agendamentos:agendamentos')
    raise_exception = True
    
    
class AgendamentoListView(LoginRequiredMixin, ListView):
    """View para listar os agendamentos."""
    model = Agendamento
    template_name = 'agendamentos/listagem_agendamentos.html'
    paginate_by = 10
    context_object_name = 'agendamentos'
    ordering = ['cliente']
    raise_exception = True


class AgendamentoDetailView(LoginRequiredMixin, DetailView):
    """View para detalhar os dados de um agendamento."""
    model = Agendamento
    template_name = 'agendamentos/detalhes_agendamento.html'
    context_object_name = 'agendamento'
    raise_exception = True


class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    """View para atualizar os dados de uma agendamento."""
    model = Agendamento
    template_name = 'agendamentos/atualizar_agendamento.html'
    fields = ['profissional', 'servico', 'data_hora']
    success_url = reverse_lazy('agendamentos:agendamentos')
    raise_exception = True


class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    """View para deletar um agendamento."""
    model = Agendamento
    template_name = 'agendamentos/deletar_agendamento.html'
    context_object_name = 'agendamento'
    success_url = reverse_lazy('agendamentos:agendamentos')
    raise_exception = True