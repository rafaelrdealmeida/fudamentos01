import requests
from bs4 import BeautifulSoup
# import pandas as pd

#TODO: extrair as demais infos - ok
#TODO: percorrer as demais paginas - ok
#TODO: extrai o conteudo (paragrafos) de cada link
#TODO: inserir as infos em um arquivo JSON
#TODO: Webcraping Selenium

def acessar_pagina(link):
    """
    Responsavel por acessar as paginas web
    """
    pagina = requests.get(link)
    bs = BeautifulSoup(pagina.text, 'html.parser')
    # print(bs)
    return bs

def extrair_infos(percorre_paginas):
    """
    Responsavel extrair as informações
    #link = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int=30"
    recebe como parametro no lista de urls
    """
    for link in percorre_paginas:
        pagina = acessar_pagina(link)
        # div id="content-core"
        notas_imprensa = pagina.find("div", attrs={"id":"content-core"}).find_all("article") 
        # print(notas_imprensa)
        for nota_imprensa in notas_imprensa:
            titulo = nota_imprensa.find('h2').text.strip()
            link =  nota_imprensa.a["href"]
            # tag_span é uma lista com tres elementos ["data", "horário", "noticias"]
            tag_span_data_horario = nota_imprensa.find_all("span", attrs={"class":"summary-view-icon"})
            data = tag_span_data_horario[0].text.strip()
            horario = tag_span_data_horario[1].text.strip()
            numero_nota = nota_imprensa.find("span", attrs={"class":"subtitle"}).text.strip().split(" ")[-1]
            print(titulo)
            print(link)
            print(data)
            print(horario)
            print(numero_nota, type(numero_nota))
            #EXTRAIR paragrafos (acessar o link, e pegar os paragrafos)
            print("###")

def percorrer_paginas():
    """
    Reponsável por percorrer as paginas em que os links estão disponiveis
    e retornar uma lista de links com as notas
    """
    lista_paginas = []
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int="
    contador = 120
    while contador >= 0:
        link_page = url  + str(contador)
        
        lista_paginas.append(link_page)
        contador = contador - 30
    return lista_paginas
        

def inserir_infos_banco():
    pass


def main():
    # extrair_infos()
    percorre_paginas = percorrer_paginas()
    extrair_infos(percorre_paginas)


if __name__ == "__main__":
    main()