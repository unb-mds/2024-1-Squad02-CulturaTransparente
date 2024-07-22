import os

def verNomeMunicipio(arquivo):
    nome_arquivo = os.path.splitext(arquivo)[0]
    partesDonome = nome_arquivo.split("_")
    nomeDomunicipio = ' '.join(partesDonome[:-1])
    return nomeDomunicipio.title()
