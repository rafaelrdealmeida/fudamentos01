import requests
from bs4 import BeautifulSoup
# import pandas as pd

#TODO: extrair as demais infos - ok
#TODO: percorrer as demais paginas - ok
#TODO: try e except - ok
#TODO: Alguns números das notas estão sendo coletados da seguinte maneira: 636/2008. Deixe a variável numero_nota apenas com o numero sem ao /2008 - ok
#TODO: extrair paragrafos e data e horario de atualização - ok
#TODO: inserir as infos em um arquivo JSON
#TODO: Webcraping Selenium
#TODO: Analise de dados

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
        for nota_imprensa in notas_imprensa: # [nota01,nota02...]
            titulo = nota_imprensa.find('h2').text.strip()
            link =  nota_imprensa.a["href"]
            # tag_span é uma lista com tres elementos ["data", "horário", "noticias"]
            tag_span_data_horario = nota_imprensa.find_all("span", attrs={"class":"summary-view-icon"})
            data = tag_span_data_horario[0].text.strip()
            horario = tag_span_data_horario[1].text.strip()
            # "NOTA À IMPRENSA Nº 636/2008" >> ["NOTA", "À", "IMPRENSA", "Nº", "636/2008"]
            # numero_nota = nota_imprensa.find("span", attrs={"class":"subtitle"}).text.strip().split(" ")[-1]
            try:
                numero_nota = nota_imprensa.find("span", attrs={"class":"subtitle"}).text.strip().split("/")[-1]    
            except AttributeError as erro:
                if str(erro) == "'NoneType' object has no attribute 'text'":   
                    numero_nota = "NA"
            if numero_nota != "NA":
                verificar = numero_nota.find("/")
                # 15/1997 >> ["15", "1997"]
                if verificar != 0:
                    numero_nota = numero_nota.split("/")[0]
            
            print(titulo)
            print(link)
            print(data)
            print(horario)
            print(numero_nota, type(numero_nota))
            #EXTRAIR paragrafos (acessar o link, e pegar os paragrafos)
            conteudo = acessar_pagina(link)
            # class="documentModified"
            data_horario_atualizado = conteudo.find("span", attrs={"class":"documentModified"}).text.strip().split(" ")
            print(data_horario_atualizado)
            # 'em\n31/10/2022'
            data_atualizada =  data_horario_atualizado[-2][3:]
            horario_atualizado =  data_horario_atualizado[-1]
            print(data_atualizada)
            print(horario_atualizado)
            # property="rnews:articleBody"
            lista_paragrafos = conteudo.find("div", attrs={"property": "rnews:articleBody"}).find_all("p")
            paragrafos = []
            for tag_p in lista_paragrafos:
                paragrafo = tag_p.text.strip()
                paragrafos.append(paragrafo)
            print(paragrafos)

            print("###")

def percorrer_paginas():
    """
    Reponsável por percorrer as paginas em que os links estão disponiveis
    e retornar uma lista de links com as notas
    """
    lista_paginas = []
    url = "https://www.gov.br/mre/pt-br/canais_atendimento/imprensa/notas-a-imprensa/notas-a-imprensa?b_start:int="
    contador = 5010
    while contador == 5010:
        link_page = url  + str(contador)
        
        lista_paginas.append(link_page)
        contador = contador - 30
    return lista_paginas
        

def inserir_infos_banco():
    pass


def main():
    # extrair_infos()
    percorre_paginas = percorrer_paginas() # [link1,link2]
    extrair_infos(percorre_paginas)


if __name__ == "__main__":
    main()