import unittest
import os 
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from backend.functions.regex import regexMunicipio


class TestRegexMunicipio(unittest.TestCase):
    def test_arraial_do_cabo(self):
        expected = r'Secretaria Municipal de Educação, Cultura, Ciência e Tecnologia.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('arraial do cabo'), expected)
    
    def test_belford_roxo(self):
        expected = r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('belford roxo'), expected)
    
    def test_niteroi(self):
        expected = r'SECRETARIA MUNICIPAL DAS CULTURAS.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('niteroi'), expected)
    
    def test_nova_iguacu(self):
        expected = r'Secretaria Municipal de Cultura.*?(\d{1,3}(?:\.\d{3})*,\d{2})\b'
        self.assertEqual(regexMunicipio('nova iguaçu'), expected)
    
    def test_rio_de_janeiro(self):
        expected = r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('rio de janeiro'), expected)
    
    def test_sao_jose_de_mereti(self):
        expected = r'Secretaria municipal de educação, cultura e turismo.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('são josé de mereti'), expected)
    
    def test_default(self):
        expected = r'Secretaria Municipal.*?R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'
        self.assertEqual(regexMunicipio('outro municipio'), expected)


if __name__ == '__main__':
    unittest.main()