from django.db import models


class Cliente(models.Model):
    """Modelo que representa um cliente.
    
    Essa classe define os campos e comportamentos do modelo Cliente, que inclui
    o nome, telefone, email e cadastrado_em.
    
    Atributos:
        nome (CharField): O nome do cliente, com tamanho máximo de 100 
                          caracteres.
        telefone (CharField): Telefone do cliente, com tamanho máximo de 
                              11 caracteres e devendo ser único no banco de 
                              dados.
        email (EmaillField): O e-mail do cliente, devendo ser único no banco de 
                             dados.
    """
    
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(unique=True)
    cadastrado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Retorne o nome do cliente."""
        return self.nome
