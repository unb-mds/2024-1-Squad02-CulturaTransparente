import os
import re
from collections import defaultdict

def buscar_valores(arquivo):
    if not os.path.isfile(arquivo):
        print(f'O arquivo "{arquivo}" não foi encontrado.')
        return []

    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        matches = re.findall(r'R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+))\b', conteudo, re.IGNORECASE)
        return [float(valor) for valor in matches]


def verNomeMunicipio(arquivo):
    nome_arquivo = os.path.splitext(arquivo)[0]
    partes_nome = nome_arquivo.split("_")
    return partes_nome[0]

def agrupar_valores_por_municipio(pasta):
    if not os.path.isdir(pasta):
        print(f'A pasta "{pasta}" não foi encontrada.')
        return

    arquivos = os.listdir(pasta)
    somas_por_municipio = defaultdict(float)

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            valores_encontrados = buscar_valores(caminho_arquivo)
            municipio = verNomeMunicipio(arquivo)
            somas_por_municipio[municipio] += sum(valores_encontrados)

    return somas_por_municipio

def salvar_somas_por_municipio(pasta, somas_por_municipio):
    pasta_valores_agrupados = os.path.join(pasta, 'valores_agrupados')
    if not os.path.exists(pasta_valores_agrupados):
        os.makedirs(pasta_valores_agrupados)

    for municipio, soma in somas_por_municipio.items():
        caminho_arquivo_soma = os.path.join(pasta_valores_agrupados, f'{municipio}_soma.txt')
        with open(caminho_arquivo_soma, 'w', encoding='utf-8') as f:
            f.write(str(soma))

pasta = "./data_collection/gazette/spiders/rj/data"

somas_por_municipio = agrupar_valores_por_municipio(pasta)

salvar_somas_por_municipio(pasta, somas_por_municipio)
