from django.test import TestCase
from model_mommy import mommy

class ProdutoTestCase(TestCase):
    def setUp(self):
        self.produto = mommy.make('Produto')

    def test_str(self):
        self.assertEquals(str(self.produto), self.produto.nome)


