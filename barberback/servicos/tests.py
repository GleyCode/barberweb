from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Servico


class ServicoModelTest(TestCase):
    """Caso de teste para o modelo Servico."""
    
    @classmethod
    def setUpTestData(cls):
        """Crie uma instância de Servico para que seja testada."""
        Servico.objects.create(nome="Corte de Cabelo", descricao="Corte masculino", preco=50.00)
        
    def test_representacao_objeto(self):
        """Teste a saída do método __str__.
        
        Esse método deve retornar uma representação em string do modelo 
        Servico. 
        """
        servico = Servico.objects.get(id=1)
        self.assertEqual(servico.__str__(), "[Corte de Cabelo - Corte masculino - R$ 50.00]")
        
    def test_tamanho_nome(self):
        """Teste o campo 'nome' para validar o tamanho correto.
        
        O campo 'nome' tem o tamanho de no máximo 100 caracteres.
        """
        servico = Servico.objects.get(id=1)
        tamanho_max = servico._meta.get_field('nome').max_length
        self.assertEqual(tamanho_max, 100)

    def test_tamanho_descricao(self):
        """Teste o campo 'descricao' para validar o tamanho.
        
        O campo 'descricao' deve ter o tamanho de 255 caracteres totais.
        """
        servico = Servico.objects.get(id=1)
        tamanho_max = servico._meta.get_field('descricao').max_length
        self.assertEqual(tamanho_max, 255)
        
    def test_formatacao_preco(self):
        """Teste o campo 'preco' para validar a formatação.
        
        O campo 'preco' deve ter o formato correto, 5 dígitos totais, 
        sendo 2 decimais.
        """
        servico = Servico.objects.get(id=1)
        num_max_digitos = servico._meta.get_field('preco').max_digits
        num_casas_decimais = servico._meta.get_field('preco').decimal_places
        self.assertEqual(num_max_digitos, 5)
        self.assertEqual(num_casas_decimais, 2)
        

class ServicoViewTest(TestCase):
    """Caso de teste para as views do modelo Servico."""
    
    def setUp(self):
        """Crie e autentique um usuário para testar as views."""
        self.usuario = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")

    def test_acesso_autenticado_servicos(self):
        """Teste se o código HTTP é 200.
        
        O status HTTP 200 indica que o usuário consegue acessar a área de 
        gerencimento de serviços estando autenticado.
        """
        resposta = self.client.get(reverse("servicos:servicos"))
        self.assertEqual(resposta.status_code, 200)
        
    def test_acesso_acesso_desautenticado_servicos(self):
        """Teste se o status HTTP é 403.
        
        O status HTTP 403 indica que o acesso à área de gerenciamento de 
        serviços a clientes não autenticados está indisponível.
        """
        self.client.logout()
        resposta = self.client.get(reverse("servicos:servicos"))
        self.assertEqual(resposta.status_code, 403)
        
    def test_acesso_desautenticado_cadastrar_servico(self):
        """Teste se o status HTTP é 403.
        
        O status HTTP 403 indica que o acesso a área de cadastro de serviço a 
        clientes não autenticados está indisponível.
        """
        self.client.logout()
        resposta = self.client.get(reverse("servicos:cadastrar_servico"))
        self.assertEqual(resposta.status_code, 403)
        
    def test_acesso_desautenticado_atualizar_servico(self):
        """Teste se o status HTTP é 403.
        
        O status HTTP 403 indica que o acesso a área de atualização de serviço 
        a clientes não autenticados está indisponível.
        """
        self.client.logout()
        resposta = self.client.get(reverse("servicos:atualizar_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_desautenticado_detalhes_servico(self):
        """Teste se o status HTTP é 403.
        
        O status HTTP 403 indica que o acesso a área de detalhamento de serviço 
        a clientes não autenticados está indisponível.
        """
        self.client.logout()
        resposta = self.client.get(reverse("servicos:detalhes_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_desautenticado_deletar_servico(self):
        """Teste se o status HTTP é 403.
        
        O status HTTP 403 indica que o acesso a área de exclusão de serviço a 
        clientes não autenticados está indisponível.
        """
        self.client.logout()
        resposta = self.client.get(reverse("servicos:deletar_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
