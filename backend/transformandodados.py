import os
import re
from collections import defaultdict

def buscar_valores(arquivo, regex):
    """Busca valores em um arquivo usando uma regex fornecida."""
    if not os.path.isfile(arquivo):
        print(f'O arquivo "{arquivo}" não foi encontrado.')
        return []

    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        matches = re.findall(regex, conteudo, re.IGNORECASE)
        # Converte valores para float e substitui vírgula por ponto
        return [float(valor.replace(',', '.')) for valor in matches]

def verNomeMunicipio(arquivo):
    """Extrai o nome do município a partir do nome do arquivo."""
    nome_arquivo = os.path.splitext(arquivo)[0]
    partes_nome = nome_arquivo.split("_")
    return partes_nome[0].lower()

def regex_por_municipio(municipio):
    """Retorna a regex específica para cada município."""
    regex_dict = {
        'arraial do cabo': r'Secretaria Municipal de Educação, Cultura, Ciência e Tecnologia.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'belford roxo': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'niteroi': r'SECRETARIA MUNICIPAL DAS CULTURAS.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'nova iguaçu': r'Secretaria Municipal de Cultura.*?(\d{1,3}(?:\.\d{3})*,\d{2})\b',
        'rio de janeiro': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'são josé de mereti': r'Secretaria municipal de educação, cultura e turismo.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
    }
    # Retorna a regex correspondente ao município, ou uma regex padrão que inclui 'PREFEITURA MUNICIPAL' como prefixo
    return regex_dict.get(municipio, r'Secretaria municipal.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b')


def formatar_valor(valor):
    """Formata o valor como string, substituindo ponto por vírgula e adicionando pontos para separação de milhar."""
    partes = f"{valor:,.2f}".split(".")
    parte_inteira = partes[0].replace(",", ".")
    parte_decimal = partes[1]
    return f"{parte_inteira},{parte_decimal}"

def agrupar_valores_por_municipio(pasta):
    """Agrupa valores por município a partir dos arquivos em uma pasta."""
    if not os.path.isdir(pasta):
        print(f'A pasta "{pasta}" não foi encontrada.')
        return

    arquivos = os.listdir(pasta)
    somas_por_municipio = defaultdict(float)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            municipio = verNomeMunicipio(arquivo)
            regex = regex_por_municipio(municipio)
            valores_encontrados = buscar_valores(caminho_arquivo, regex)
            soma_valores = sum(valores_encontrados)
            somas_por_municipio[municipio] += soma_valores

    return somas_por_municipio

def salvar_somas_por_municipio(pasta, somas_por_municipio):
    """Salva as somas dos valores agrupados por município em arquivos separados."""
    pasta_valores_agrupados = os.path.join(pasta, 'valores_agrupados')
    if not os.path.exists(pasta_valores_agrupados):
        os.makedirs(pasta_valores_agrupados)

    for municipio, soma in somas_por_municipio.items():
        soma_formatada = formatar_valor(soma)
        caminho_arquivo_soma = os.path.join(pasta_valores_agrupados, f'{municipio}_soma.txt')
        with open(caminho_arquivo_soma, 'w', encoding='utf-8') as f:
            f.write(f'{soma_formatada}\n')


pasta = './2024-1-Squad02-CulturaTransparente/backend/arquivos_nomeados'

somas_por_municipio = agrupar_valores_por_municipio(pasta)


salvar_somas_por_municipio(pasta, somas_por_municipio)
