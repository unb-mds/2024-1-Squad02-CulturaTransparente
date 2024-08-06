from .group import agrupar
from .sums import salvarSomas

def principal():
    pasta = "../.gitignore/arquivos_renomeados"
    
    somasTotais = agrupar(pasta)
    
    if somasTotais:
        salvarSomas(pasta, somasTotais)

if __name__ == "__main__":
    principal()
