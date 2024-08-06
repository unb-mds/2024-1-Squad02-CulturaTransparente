import os

def meseano(arquivo):
    nome_arquivo = os.path.splitext(arquivo)[0]
    partesDonome = nome_arquivo.split("_")
    
    if len(partesDonome) > 1:
        parte_data = partesDonome[-1]
        data = parte_data.split('-')
        
        if len(data) > 1:
            ano = data[0]
            mes = data[1]
            return ano, mes
    
    return None, None
