from django.db import models


class Profissional(models.Model):
    """Modelo que representa um profissional."""
    nome = models.CharField(max_length=100)

    def __str__(self):
        """Cria e retorna uma string com os dados do profissional."""
        dados = Profissional.objects.get(id=self.id)
        return f"[{dados.id} - {self.nome}]"
