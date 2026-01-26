from django.db import models


class Servico(models.Model):
    """Modelo que representa um serviço disponível.
    
    Essa classe define os campos e comportamentos do modelo Servico, que inclui
    o nome, descrição e preço do serviço.
    
    Atributos:
        nome (CharField): O nome do serviço, com tamanho máximo de 100 caracteres.
        descricao (CharField): A descrição do serviço, com tamanho máximo de 255 caracteres.
        preco (DecimalField): O preço do serviço, com até 5 dígitos no total, sendo 2 decimais.
    """
    
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """Retorne uma string com os dados do serviço."""
        dados = f"[{self.nome} - {self.descricao} - R$ {self.preco}]"
        return dados
