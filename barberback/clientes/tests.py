from django.db.utils import IntegrityError
from django.test import TestCase

from .models import Cliente


class ClienteModelTest(TestCase):
    """Conjunto de testes para o modelo Cliente."""
    @classmethod
    def setUpTestData(cls):
        """Esse método é usado para configurar um objeto do tipo Cliente que 
        servirá para todos os métodos de teste desta classe.
        """
        Cliente.objects.create(nome="Cliente Teste", telefone="00000000000",email="teste@gmail.com")
    
    
    #def setUp(self):
    #    """Esse método é usado para criar uma instancia por método de teste do #    Cliente.
    #    """
    #    Cliente.objects.create(nome="Cliente Teste", telefone="00000000000",#    email="teste@gmail.com")
    
    #def tearDown(self):
    #    """Esse método é usado para limpar os dados após cada teste. Nessa 
    #    classe não será utilizado pois o Django já cuida da destruição do 
    #    banco de dados e dos objetos criados por debaixo dos panos.
    #    """
    #    pass
    
    def test_representacao_str(self):
        """Esse método testa a representação em string do modelo Cliente. Verificando se o método __str__ retorna a string formatada corretamente."""
        cliente1 = Cliente.objects.get(id=1)
        self.assertEqual(cliente1.__str__(), "[Cliente Teste - 00000000000 - teste@gmail.com]")

    def test_tamanho_do_nome(self):
        """"""
        cliente = Cliente.objects.get(id=1)
        tamanho_max = cliente._meta.get_field('nome').max_length
        self.assertEqual(tamanho_max, 100)
        
    def test_tamanho_do_telefone(self):
        """O método verificar se o campo 'telefone' está armazenando contatos 
        com 11 digítos, que é o formato atual no Brasil.
        """
        cliente = Cliente.objects.get(id=1)
        tamanho_max = cliente._meta.get_field('telefone').max_length
        self.assertEqual(tamanho_max, 11)
        
    def test_telefone_unico(self):
        """Esse método verifica se o campo 'telefone' do modelo está corretamente configurado para receber valores únicos.
        """
        cliente = Cliente.objects.get(id=1)
        status_telefone_unico = cliente._meta.get_field('telefone').unique
        self.assertTrue(status_telefone_unico)

    def test_email_unico(self):
        """Esse método verifica se o campo 'email' do modelo está corretamente configurado para receber valores únicos.
        """
        cliente = Cliente.objects.get(id=1)
        status_email_unico = cliente._meta.get_field('email').unique
        self.assertTrue(status_email_unico)

    def test_data_hora_cadastrado_automaticamente(self):
        """"""
        cliente = Cliente.objects.get(id=1)
        status_datetime = cliente._meta.get_field('cadastrado_em').auto_now_add
        self.assertTrue(status_datetime)