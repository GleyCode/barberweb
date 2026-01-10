from django.db import models

from clientes.models import Cliente
from profissionais.models import Profissional
from servicos.models import Servico


class Agendamento(models.Model):
    """Modelo que representa um agendamento."""
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    data_hora = models.DateTimeField()

    
    def __str__(self):
        """Cria e retorna uma string com os dados do agendamento."""
        dados = Agendamento.objects.get(id=self.id)
        return f"{dados.id} - {dados.cliente.nome} - {dados.profissional.nome} - {dados.servico.nome} - {self.data_hora}"
