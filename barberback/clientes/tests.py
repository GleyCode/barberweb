from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Cliente


class ClienteModelTest(TestCase):
    """Caso de teste para o modelo Cliente."""
    
    @classmethod
    def setUpTestData(cls):
        """Esse método é usado para configurar um objeto do tipo Cliente que servirá para todos os 
        métodos de teste desta classe."""
        Cliente.objects.create(nome="Cliente Teste", telefone="00000000000",email="teste@gmail.com")
    
    def test_representacao_str(self):
        """Esse método testa a representação em string do modelo Cliente. Verificando se o método 
        __str__ retorna a string formatada corretamente."""
        cliente1 = Cliente.objects.get(id=1)
        self.assertEqual(cliente1.__str__(), "[Cliente Teste - 00000000000 - teste@gmail.com]")

    def test_tamanho_do_nome(self):
        """Testa se o campo 'nome' tem o tamanho correto."""
        cliente = Cliente.objects.get(id=1)
        tamanho_max = cliente._meta.get_field('nome').max_length
        self.assertEqual(tamanho_max, 100)
        
    def test_tamanho_do_telefone(self):
        """O método verificar se o campo 'telefone' está armazenando contatos com 11 digítos, que é 
        o formato atual no Brasil."""
        cliente = Cliente.objects.get(id=1)
        tamanho_max = cliente._meta.get_field('telefone').max_length
        self.assertEqual(tamanho_max, 11)
        
    def test_telefone_unico(self):
        """Esse método verifica se o campo 'telefone' do modelo está corretamente configurado para 
        receber valores únicos."""
        cliente = Cliente.objects.get(id=1)
        status_telefone_unico = cliente._meta.get_field('telefone').unique
        self.assertTrue(status_telefone_unico)

    def test_email_unico(self):
        """Esse método verifica se o campo 'email' do modelo está corretamente configurado para 
        receber valores únicos."""
        cliente = Cliente.objects.get(id=1)
        status_email_unico = cliente._meta.get_field('email').unique
        self.assertTrue(status_email_unico)

    def test_data_hora_cadastrado_automaticamente(self):
        """Testa se o campo 'cadastrado_em' está registrando a data e a hora de forma automática."""
        cliente = Cliente.objects.get(id=1)
        status_datetime = cliente._meta.get_field('cadastrado_em').auto_now_add
        self.assertTrue(status_datetime)
        

class ClienteViewTest(TestCase):
    """Caso de teste para as views relacionadas ao modelo Cliente."""
    
    def setUp(self):
        """Esse método é usado para criar um usuário e autentica-lo antes de cada método 
        de teste."""
        self.usuario = User.objects.create_user(username="teste", password="12345")
        self.client.login(username="teste", password="12345")
        
    def test_acesso_autenticado_clientes(self):
        """Testa se o código HTTP é 200, o que significa que o usuário consegue acessar a 
        área de gerencimento de clientes estando autenticado.
        """
        resposta = self.client.get(reverse("clientes:clientes"))
        self.assertEqual(resposta.status_code, 200)
        
    def test_acesso_acesso_desautenticado_clientes(self):
        """Testa se o código HTTP é 403, o que significa que o usuário não consegiu 
        acessar a área de gerenciamento de clientes, estando desautenticado."""
        self.client.logout()
        resposta = self.client.get(reverse("clientes:clientes"))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_acesso_desautenticado_cadastrar_cliente(self):
        """Testa se o código HTTP é 403, o que significa que o usuário não consegiu 
        acessar a área de cadastro decliente, estando desautenticado."""
        self.client.logout()
        resposta = self.client.get(reverse("clientes:cadastrar_cliente"))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_acesso_desautenticado_atualizar_cliente(self):
        """Testa se o código HTTP é 403, o que significa que o usuário não consegiu 
        acessar a área de atualização do cadastro de cliente, estando desautenticado."""
        self.client.logout()
        resposta = self.client.get(reverse("clientes:atualizar_cliente", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_acesso_desautenticado_detalhes_cliente(self):
        """Testa se o código HTTP é 403, o que significa que o usuário não consegiu 
        acessar a área de detalhamento de cliente, estando desautenticado."""
        self.client.logout()
        resposta = self.client.get(reverse("clientes:detalhes_cliente", args=[1]))
        self.assertEqual(resposta.status_code, 403)
    
    def test_acesso_acesso_desautenticado_deletar_cliente(self):
        """Testa se o código HTTP é 403, o que significa que o usuário não consegiu 
        acessar a área de exclusão de cliente, estando desautenticado."""
        self.client.logout()
        resposta = self.client.get(reverse("clientes:deletar_cliente", args=[1]))
        self.assertEqual(resposta.status_code, 403)
