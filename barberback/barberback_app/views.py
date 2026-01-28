from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from agendamentos.models import Agendamento


class IndexView(LoginRequiredMixin, ListView):
    """Lista os cinco próximos agendamentos do dia.
    
    Essa view utiliza o mixin LoginRequiredMixin para garantir que apenas
    usuários autenticados possam acessar a página de dashboard. 
    Também utiliza a classe ListView do Django para facilitar o processo de 
    exibição de uma lista de objetos do modelo Agendamento.
    
    Atributos:
        template_name: O nome do template HTML que será renderizado para a
                       página de dashboard.
        context_object_name: O nome do contexto que será utilizado no template
                             para referenciar a lista de agendamentos.
        raise_exception: Define se uma exceção deve ser levantada quando um
                         usuário não autenticado tenta acessar a view.
                         
    Métodos:
        get_queryset: O método ordena os agendamentos por data e hora e passa 
                      para context_object_name os cinco próximos agendamentos.
    """
    
    template_name = "barberback_app/index.html"
    context_object_name = "agendamentos"
    raise_exception = True
    
    def get_queryset(self):
        """Retorne os cinco próximos agendamentos ordenados por data e hora."""
        return Agendamento.objects.all().order_by('data_hora')[:5]
