def regexMunicipio(municipio):
    regex_dict = {
        'arraial do cabo': r'Secretaria Municipal de Educação, Cultura, Ciência e Tecnologia.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'belford roxo': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'niteroi': r'SECRETARIA MUNICIPAL DAS CULTURAS.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'nova iguaçu': r'Secretaria Municipal de Cultura.*?(\d{1,3}(?:\.\d{3})*,\d{2})\b',
        'rio de janeiro': r'SECRETARIA MUNICIPAL DE CULTURA.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
        'são josé de mereti': r'Secretaria municipal de educação, cultura e turismo.*R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b',
    }
    regex_padrao = r'Secretaria Municipal.*?R\$\s*((?:\d+\.\d+|\d+\.\d*|\.\d+|\d+,\d+))\b'

    return regex_dict.get(municipio, regex_padrao)
