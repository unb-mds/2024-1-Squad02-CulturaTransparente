from group import agrupar
from sums import salvarSomas

def principal():
    pasta = "C:\\Users\\enric\\OneDrive\\Documentos\\Programas\\Testes pra enviar\\arquivos_renomeados"
    
    somasTotais = agrupar(pasta)
    
    if somasTotais:
        salvarSomas(pasta, somasTotais)

if __name__ == "__main__":
    principal()
