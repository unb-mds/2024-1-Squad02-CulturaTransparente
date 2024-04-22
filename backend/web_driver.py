from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

navegadorUsado = webdriver.Chrome()
navegadorUsado.get('https://queridodiario.ok.org.br')

sleep(2)


gastos = navegadorUsado.find_element('input')
gastos.send_keys('')
gastos.submit()

sleep(2)

municipio = navegadorUsado.find_element('edu-city-filter')
municipio.send_keys('')
municipio.submit()


sleep(2)

periodo = navegadorUsado.find_element('app-date-picker-range')
periodo = navegadorUsado.find_element('')
periodo.submit()

sleep(2)

botao = navegadorUsado.find_element('button')
botao.click()

sleep(2)

site = BeautifulSoup(navegadorUsado.page_source, 'html.parser')

site_bonito = site.prettify()











