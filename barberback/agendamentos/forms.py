from django.forms import ModelForm
from .models import Agendamento


class CriarAgendamentoForm(ModelForm):
    """Docstring para AgendamentoForm."""
    
    class Meta:
        """Docstring para Meta."""
        model = Agendamento
        fields = '__all__'
        

class AtualizarAgendamentoForm(ModelForm):
    """Docstring para AgendamentoForm."""
    
    class Meta:
        """Docstring para Meta."""
        model = Agendamento
        fields = ['profissional', 'servico', 'data_hora']
           