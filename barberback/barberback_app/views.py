from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from agendamentos.models import Agendamento


class IndexView(LoginRequiredMixin, ListView):
    """View para a página inicial do painel administrativo."""
    
    template_name = "barberback_app/index.html"
    context_object_name = "agendamentos"
    raise_exception = True
    
    def get_queryset(self):
        """Retorne os cinco próximos agendamentos ordenados por data e hora."""
        return Agendamento.objects.all().order_by('data_hora')[:5]
