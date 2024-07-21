import os
import subprocess

# Pegando o dirretório atual do OS para trabalharmos a partir dele
DIR_INICIAL = os.getcwd()

class Main():
    def __init__(self):
        pass
    
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
        subprocess.run(["sh", "sprint_converter.sh"], cwd=DIR_INICIAL)
        subprocess.run(["sh", "sprint_renomear.sh"], cwd=DIR_INICIAL)

    # Método para executar o código de Regex que trata os dados dos TXTs
    def start_data_transform(self):
        subprocess.run(["python3", "transformandodados.py"], cwd=DIR_INICIAL)


# Executando todos os métodos para realizar toda a operação do Backend
main = Main()
main.run_spiders_all()
main.start_sh()
main.start_data_transform()