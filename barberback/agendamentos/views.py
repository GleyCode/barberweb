from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, 
                                  DetailView)
from .models import Agendamento


class AgendamentoCreateView(LoginRequiredMixin, CreateView):
    """Docstring para AgendamentoCreateView"""
    model = Agendamento
    template_name = 'agendamentos/criar_agendamento.html'
    fields = ['cliente', 'profissional', 'servico', 'data_hora']
    success_url = reverse_lazy('agendamentos:agendamentos')
    raise_exception = True
    
    
class AgendamentoListView(LoginRequiredMixin, ListView):
    """Docstring para AgendamentoListView"""
    model = Agendamento
    template_name = 'agendamentos/listagem_agendamentos.html'
    paginate_by = 10
    context_object_name = 'agendamentos'
    ordering = ['cliente']
    raise_exception = True


class AgendamentoDetailView(LoginRequiredMixin, DetailView):
    """Docstring para AgendamentoDetailView"""
    model = Agendamento
    template_name = 'agendamentos/detalhes_agendamento.html'
    context_object_name = 'agendamento'
    raise_exception = True


class AgendamentoUpdateView(LoginRequiredMixin, UpdateView):
    """Docstring para AgendamentoUpdateView"""
    pass


class AgendamentoDeleteView(LoginRequiredMixin, DeleteView):
    """Docstring para AgendamentoDeleteView"""
    pass