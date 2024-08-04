import unittest
from unittest.mock import patch, call
import os
import subprocess

class Main():
    def _init_(self):
        self.DIR_INICIAL = os.getcwd()
    
    # Método que executa todos os spiders disponíveis
    def run_spiders_all(self):
        # Criando uma variável com o caminho dos spiders
        path = "data_collection/gazette/spiders/rj"

        # Executando todos os spiders
        subprocess.run(["scrapy", "runspider", "rj_arraial_do_cabo.py"], cwd=path)
        subprocess.run(["scrapy", "runspider", "rj_belford_roxo.py"], cwd=path)
        subprocess.run(["scrapy", "runspider", "rj_niteroi.py"], cwd=path)
        subprocess.run(["scrapy", "runspider", "rj_nova_iguacu.py"], cwd=path)
        subprocess.run(["scrapy", "runspider", "rj_rio_de_janeiro.py"], cwd=path)
        subprocess.run(["scrapy", "runspider", "rj_sao_joao_de_meriti.py"], cwd=path)

    # Método para executar os scripts para converter os arquivos para TXT e depois renomeá-los
    def start_sh(self):
        self.DIR_INICIAL = os.getcwd()
        subprocess.run(["sh", "sprint_converter.sh"], cwd=self.DIR_INICIAL)
        subprocess.run(["sh", "sprint_renomear.sh"], cwd=self.DIR_INICIAL)

    # Método para executar o código de Regex que trata os dados dos TXTs
    def start_data_transform(self):
        self.DIR_INICIAL = os.getcwd()
        subprocess.run(["python3", "main.py"], cwd=self.DIR_INICIAL)

class TestMain(unittest.TestCase):

    @patch('subprocess.run')
    def test_run_spiders_all(self, mock_run):
        main = Main()
        main.run_spiders_all()
        
        path = "data_collection/gazette/spiders/rj"
        expected_calls = [
            call(["scrapy", "runspider", "rj_arraial_do_cabo.py"], cwd=path),
            call(["scrapy", "runspider", "rj_belford_roxo.py"], cwd=path),
            call(["scrapy", "runspider", "rj_niteroi.py"], cwd=path),
            call(["scrapy", "runspider", "rj_nova_iguacu.py"], cwd=path),
            call(["scrapy", "runspider", "rj_rio_de_janeiro.py"], cwd=path),
            call(["scrapy", "runspider", "rj_sao_joao_de_meriti.py"], cwd=path)
        ]
        
        mock_run.assert_has_calls(expected_calls, any_order=True)

    @patch('subprocess.run')
    @patch('os.getcwd', return_value='/fake/dir')
    def test_start_sh(self, mock_getcwd, mock_run):
        main = Main()
        main.start_sh()

        expected_calls = [
            call(["sh", "sprint_converter.sh"], cwd='/fake/dir'),
            call(["sh", "sprint_renomear.sh"], cwd='/fake/dir')
        ]
        
        mock_run.assert_has_calls(expected_calls, any_order=True)

    @patch('subprocess.run')
    @patch('os.getcwd', return_value='/fake/dir')
    def test_start_data_transform(self, mock_getcwd, mock_run):
        main = Main()
        main.start_data_transform()

        mock_run.assert_called_once_with(["python3", "main.py"], cwd='/fake/dir')

if __name__ == '__main__':
    unittest.main()