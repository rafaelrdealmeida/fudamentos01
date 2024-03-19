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
from datetime import datetime


#TODO: Webcraping Selenium
# https://github.com/SergeyPirogov/webdriver_manager
#TODO: Analise de dados

def acessar_pagina_dinamica(link):
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link)

    contador = 0
    while contador < 2:
        encontrar = navegador.find_element(By.CSS_SELECTOR, "#ano").find_elements(By.TAG_NAME, "option")  # ["2024", "2023", "2022"]
        # click no ano
        encontrar[contador].click()
        # click no pesquisar
        navegador.find_element(By.CSS_SELECTOR,"#button1").click()

        #content > table > tbody > tr:nth-child(2) > td:nth-child(1) > table > tbody > tr:nth-child(5) > td:nth-child(4)
        dias = navegador.find_elements(By.CSS_SELECTOR, '.calWeekDaySel, .calWeekEndSel') # [day1pdf, day2pdf...]
        print(len(dias))
        for dia in dias:
            ######
            # nomear os arquivos pdfs
            #####
            tag_a = dia.find_element(By.TAG_NAME, "a")
            #["dc_20b.asp?selCodColecaoCsv=D&amp;Datain","6/2/2024"]
            atributo_href = tag_a.get_attribute("href") # link do pdf
            data_string = atributo_href.split("=")[-1]
            data = datetime.strptime(data_string, "%d/%m/%Y")
            data_formatada = data.strftime("%Y-%m-%d") # 2024-06-02
            # print(data_formatada)
            # "dc_20b.asp?selCodColecaoCsv=D&amp;Datain=6/2/2024"
            # https://imagem.camara.leg.br/montaPdf.asp?narquivo=DCD0020240206000020000.PDF&npagina=
            # https://imagem.camara.gov.br/Imagem/d/pdf/DCD0020240206000020000.PDF#page=

            link_pdf_final = redirecionamento_pdf(atributo_href) # link final do pdf
            coleta_pdf = requests.get(link_pdf_final)
            if  coleta_pdf.status_code == 200:
                with open (f'{data_formatada}.pdf', "wb") as arquivo:
                    arquivo.write(coleta_pdf.content)
            else:
                print(f"PDF inexistente. Status code; {coleta_pdf.status_code}")
        contador = contador + 1
        sleep (3)

def redirecionamento_pdf(link_pdf_final):
    navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    navegador.get(link_pdf_final)
    link_anterior = navegador.current_url # armazena o primeiro redirecionamento
    while True:
        sleep(2)
        link_atual = navegador.current_url
        if link_atual != link_anterior:
            link_anterior = link_atual
            continue
        else:
            navegador.quit()
            print(link_atual)
            return link_atual

        



def main():
    link = "https://imagem.camara.leg.br/pesquisa_diario_basica.asp"
    acessar_pagina_dinamica(link)
    


if __name__ == "__main__":
    main()