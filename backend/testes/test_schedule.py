import unittest
import os 
import sys 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..')))
from backend.functions.schedule import meseano

class TestMeseano(unittest.TestCase):
    
    def teste_arquivo_valido(self):
        self.assertEqual(meseano('relatorio_2023-07.txt'), ('2023', '07'))
    
    def teste_valido_arquivo_formato_diferente(self):
        self.assertEqual(meseano('dados_2021-12.csv'), ('2021', '12'))

    def test_invalido_arquivo_sem_data(self):
        self.assertEqual(meseano('arquivo_sem_data.txt'), (None, None))
    
    def test_invalido_arquivo_formato_errado(self):
        self.assertEqual(meseano('relatorio_2022_07.txt'), (None, None))

    def test_sem_arquivo(self):
        self.assertEqual(meseano(''), (None, None))
    
    def test_arquivo_sem_extensao(self):
        self.assertEqual(meseano('relatorio_2023-07'), ('2023', '07'))
    
    def test_arquivo_com_nome_composto(self):
        self.assertEqual(meseano('backup_arquivos_relatorio_2024-06.txt'), ('2024', '06'))

if __name__ == '__main__':
    unittest.main()