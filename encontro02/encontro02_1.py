import requests
from bs4 import BeautifulSoup
import pandas as pd


def acessar_pagina(link):
    """
    Responsavel por acessar as paginas web
    """
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    # print(bs)
    return bs

def extrair_infos():
    link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa"
    pagina = acessar_pagina(link)
    # div id="content-core"
    notas_imprensa = pagina.find("div", attrs={"id":"content-core"}).find_all("article") 
    # print(notas_imprensa)
    for nota_imprensa in notas_imprensa:
        titulo = nota_imprensa.find('h2').text.strip()
        print(titulo)
        print("###")
    print("fim do loop for")


    

def main():
    extrair_infos()

if __name__ == "__main__":
    main()