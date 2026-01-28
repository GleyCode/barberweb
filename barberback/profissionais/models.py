from django.db import models


class Profissional(models.Model):
    """Modelo que representa um serviço disponível.
    
    Essa classe define os campos e comportamentos do modelo Profissional, que 
    inclui o nome.
    
    Atributos:
        nome (CharField): O nome do profissional, com tamanho máximo de 100 
                          caracteres.
    """
    nome = models.CharField(max_length=100)

    def __str__(self):
        """Crie e retorne uma string com os dados do profissional."""
        dados = Profissional.objects.get(id=self.id)
        return f"[{dados.id} - {self.nome}]"
