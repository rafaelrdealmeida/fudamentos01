# imports do beautifulsoap
import requests
from bs4 import BeautifulSoup
# imports do selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep


#TODO: Webcraping Selenium
# https://github.com/SergeyPirogov/webdriver_manager
#TODO: Analise de dados

def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)
    # este codigo comentado faz as ações em um ano específico
    # tag_anos = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")
    # anos = []
    # for tag_ano in tag_anos:
    #     ano = tag_ano
    #     anos.append(ano)

    # data = anos[2]
    # data.click()
    # sleep (10)
    # botoa_pesquisar = navegador.find_element(By.CSS_SELECTOR,"#button1").click()
    # sleep (10)

    contador = 0
    while contador < 10:
        encontrar = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")  # ["2024", "2023", "2022"]
        # click no ano
        encontrar[contador].click()
        # click no pesquisar
        navegador.find_element(By.CSS_SELECTOR,"#button1").click()
        # avaliar se é possivel passar pagina carregada para o beautifulsoap
        # ou se o selenium ainda é necessário
        # bs = BeautifulSoap(navegador.page_source, "lxml")
        # pdf_dia(bs)
        contador = contador + 1
        sleep (3)

def pdf_dia():
    """responsável por coletar os pdfs disponíveis a cada dia"""
    pass



def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    


if __name__ == "__main__":
    main()