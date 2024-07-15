import os
import re
import json
from collections import defaultdict

def buscar_valores(arquivo, regex):
    if not os.path.isfile(arquivo):
        print(f'O arquivo "{arquivo}" não foi encontrado.')
        return []

    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
        matches = re.findall(regex, conteudo, re.IGNORECASE)
        return [float(valor.replace(',', '.')) for valor in matches]

def verNomeMunicipio(arquivo):
    nome_arquivo = os.path.splitext(arquivo)[0]
    partes_nome = nome_arquivo.split("_")
    nome_municipio = ' '.join(partes_nome[:-1])
    return nome_municipio.title()

def extrair_mes(arquivo):
    nome_arquivo = os.path.splitext(arquivo)[0]
    partes_nome = nome_arquivo.split("_")
    
    if len(partes_nome) > 1:
        parte_data = partes_nome[-1]
        
        data = parte_data.split('-')
        
        if len(data) > 1:
            ano = data[0]
            mes = data[1]
            return ano, mes
    
    return None, None

def regex_por_municipio(municipio):
    regex_dict = {
        'arraial do cabo': r'Secretaria Municipal de Educação, Cultura, Ciência e Tecnologia.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'belford roxo': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'niteroi': r'SECRETARIA MUNICIPAL DAS CULTURAS.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'nova iguaçu': r'Secretaria Municipal de Cultura.*?(\d{1,3}(?:\.\d{3})*,\d{2})\b',
        'rio de janeiro': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'são josé de mereti': r'Secretaria municipal de educação, cultura e turismo.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
    }
    regex_padrao = r'Secretaria municipal.*?Cultura.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'

    return regex_dict.get(municipio, regex_padrao)

def formatar_valor(valor):
    partes = f"{valor:,.2f}".split(".")
    parte_inteira = partes[0].replace(",", ".")
    parte_decimal = partes[1]
    return f"{parte_inteira}.{parte_decimal}"

def agrupar_valores_por_municipio_e_mes(pasta):
    if not os.path.isdir(pasta):
        print(f'A pasta "{pasta}" não foi encontrada.')
        return

    arquivos = os.listdir(pasta)
    somas_por_municipio_ano_mes = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

    for arquivo in arquivos:
        caminho_arquivo = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho_arquivo):
            municipio = verNomeMunicipio(arquivo)
            ano, mes = extrair_mes(arquivo)
            regex = regex_por_municipio(municipio)
            valores_encontrados = buscar_valores(caminho_arquivo, regex)
            soma_valores = sum(valores_encontrados)
            somas_por_municipio_ano_mes[municipio][ano][mes] += soma_valores

    return somas_por_municipio_ano_mes

def salvar_somas_por_municipio_e_mes(pasta, somas_por_municipio_e_mes):
    dados_agrupados_por_ano = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))

    for municipio, anos_meses_somas in somas_por_municipio_e_mes.items():
        for ano, meses_somas in anos_meses_somas.items():
            for mes, soma in meses_somas.items():
                dados_agrupados_por_ano[ano][municipio][mes] += soma

    for ano, municipios_meses_somas in dados_agrupados_por_ano.items():
        caminho_arquivo_json = os.path.join(pasta, f'{ano}_somas.json')
        dados_json = {municipio: {mes: formatar_valor(soma) for mes, soma in meses_somas.items()} for municipio, meses_somas in municipios_meses_somas.items()}
        
        with open(caminho_arquivo_json, 'w', encoding='utf-8') as f:
            json.dump(dados_json, f, ensure_ascii=False, indent=4)

pasta = "./2024-1-Squad02-CulturaTransparente/backend/arquivos_nomeados"

somas_por_municipio_e_mes = agrupar_valores_por_municipio_e_mes(pasta)

salvar_somas_por_municipio_e_mes(pasta, somas_por_municipio_e_mes)
