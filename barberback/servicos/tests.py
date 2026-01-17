from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Servico


class ServicoModelTest(TestCase):
    """Caso de teste para o modelo Servico."""
    
    @classmethod
    def setUpTestData(cls):
        """Esse método é usado para configurar um objeto do tipo Servico que
        servirá para todos os métodos de teste desta classe."""
        Servico.objects.create(nome="Corte de Cabelo", descricao="Corte masculino", preco=50.00)
        
    def test_representacao_objeto(self):
        """Esse método testa a representação em string do modelo Servico. 
        Verificando se o método __str__ retorna a string formatada corretamente."""
        servico = Servico.objects.get(id=1)
        self.assertEqual(servico.__str__(), "[Corte de Cabelo - Corte masculino - R$ 50.00]")
        
    def test_tamanho_nome(self):
        """Testa se o campo 'nome' tem o tamanho correto."""
        servico = Servico.objects.get(id=1)
        tamanho_max = servico._meta.get_field('nome').max_length
        self.assertEqual(tamanho_max, 100)

    def test_tamanho_descricao(self):
        """Testa se o campo 'descricao' tem o tamanho correto."""
        servico = Servico.objects.get(id=1)
        tamanho_max = servico._meta.get_field('descricao').max_length
        self.assertEqual(tamanho_max, 255)
        
    def test_formatacao_preco(self):
        """Testa se o campo 'preco' tem o formato correto, 5 dígitos totais, 
        sendo 2 decimais."""
        servico = Servico.objects.get(id=1)
        num_max_digitos = servico._meta.get_field('preco').max_digits
        num_casas_decimais = servico._meta.get_field('preco').decimal_places
        self.assertEqual(num_max_digitos, 5)
        self.assertEqual(num_casas_decimais, 2)
        

class ServicoViewTest(TestCase):
    """Caso de teste para as views do modelo Servico."""
    
    def setUp(self):
        """Esse método é usado para criar um usuário e autentica-lo antes de 
        cada método de teste."""
        self.usuario = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")

    def test_acesso_autenticado_servicos(self):
        """Testa se o código HTTP é 200, o que significa que o usuário consegue 
        acessar a área de gerencimento de serviços estando autenticado."""
        resposta = self.client.get(reverse("servicos:servicos"))
        self.assertEqual(resposta.status_code, 200)
        
    def test_acesso_acesso_desautenticado_servicos(self):
        """Testa se o código HTTP é 403; que nega o acesso a área de 
        gerenciamento de serviços a clientes não autenticados."""
        self.client.logout()
        resposta = self.client.get(reverse("servicos:servicos"))
        self.assertEqual(resposta.status_code, 403)
        
    def test_acesso_desautenticado_cadastrar_servico(self):
        """Testa se o código HTTP é 403; que nega o acesso a área de 
        gerenciamento de serviços a clientes não autenticados."""
        self.client.logout()
        resposta = self.client.get(reverse("servicos:cadastrar_servico"))
        self.assertEqual(resposta.status_code, 403)
        
    def test_acesso_desautenticado_atualizar_servico(self):
        """Testa se o status HTTP é 403; que nega o acesso a área de
        atualização de serviço a clientes não autenticados."""
        self.client.logout()
        resposta = self.client.get(reverse("servicos:atualizar_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_desautenticado_detalhes_servico(self):
        """Testa se o status HTTP é 403; que nega o acesso a área de
        detalhamento de serviço a clientes não autenticados."""
        self.client.logout()
        resposta = self.client.get(reverse("servicos:detalhes_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_desautenticado_deletar_servico(self):
        """Testa se o status HTTP é 403; que nega o acesso a área de
        exclusão de serviço a clientes não autenticados."""
        self.client.logout()
        resposta = self.client.get(reverse("servicos:deletar_servico", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    