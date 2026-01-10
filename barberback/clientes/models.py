from django.db import models


class Cliente(models.Model):
    """Modelo que representa um cliente."""
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Cria e retorna uma string com os dados do cliente."""
        dados = f"[{self.nome} - {self.telefone} - {self.email}]"
        return dados
