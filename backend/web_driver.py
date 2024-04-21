from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

navegadorUsado = webdriver.Chrome()
navegadorUsado.get('https://queridodiario.ok.org.br')

# Aguarda até que o elemento do filtro de cidades seja visível
filtro_de_cidades = WebDriverWait(navegadorUsado, 10).until(
    EC.visibility_of_element_located((By.NAME, 'edu-city-filter'))
)
filtro_de_cidades.send_keys()  # Substitua 'Nome da cidade' pela cidade desejada
filtro_de_cidades.send_keys(Keys.RETURN)

# Aguarda até que o elemento do filtro de gastos seja visível
filtro_de_gastos = WebDriverWait(navegadorUsado, 10).until(
    EC.visibility_of_element_located((By.NAME, 'input'))
)
filtro_de_gastos.send_keys()  # Substitua 'Nome do gasto' pelo tipo de gasto desejado
filtro_de_gastos.send_keys(Keys.RETURN)

# Aguarda até que o botão de pesquisa seja visível
botao_de_pesquisar = WebDriverWait(navegadorUsado, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]'))
)
botao_de_pesquisar.click()

# Espera até que a página seja completamente carregada
WebDriverWait(navegadorUsado, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

# Extrai o conteúdo da página
page_content = navegadorUsado.page_source
site = BeautifulSoup(page_content, 'html.parser')