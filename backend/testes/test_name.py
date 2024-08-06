import unittest
import sys
import os 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from backend.functions.name import verNomeMunicipio

class TestVerNomeMunicipio(unittest.TestCase):

    def test_nome_municipio_simples(self):
        arquivo = "brasilia_.txt"
        nome_municipio_esperado = "Brasilia"
        nome_municipio_obtido = verNomeMunicipio(arquivo)
        self.assertEqual(nome_municipio_esperado, nome_municipio_obtido)

    def test_nome_municipio_composto(self):
        arquivo = "rio_de_janeiro_.txt"
        nome_municipio_esperado = "Rio De Janeiro"
        nome_municipio_obtido = verNomeMunicipio(arquivo)
        self.assertEqual(nome_municipio_esperado, nome_municipio_obtido)

    def test_nome_municipio_caixa_alta(self):
        arquivo = "ARRAIAL_DO_CABO_.txt"
        nome_municipio_esperado = "Arraial Do Cabo"
        nome_municipio_obtido = verNomeMunicipio(arquivo)
        self.assertEqual(nome_municipio_esperado, nome_municipio_obtido)

if __name__ == "__main__":
    unittest.main()