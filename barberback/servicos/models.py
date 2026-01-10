from django.db import models


class Servico(models.Model):
    """Modelo que representa um serviço disponível."""
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """Cria e retorna uma string com os dados do serviço."""
        dados = f"[{self.nome} - {self.descricao} - R$ {self.preco}]"
        return dados
