import requests
from bs4 import BeautifulSoup
import csv

'''
Documentação https://www.crummy.com/software/BeautifulSoup/bs4/do
site - vagas.com.br

Primeiro o programa vai pegar o total de páginas
Depois vai fazer um scrapping, pegando os detalhes relevantes dos empregos encontrados
depois vai passa para um arquivo csv
'''

# PEGANDO O NÚMERO DE PÁGINAS
def search_keyword(keywords):
  r = requests.get(f"https://www.vagas.com.br/vagas-de-{keywords}")
  html_doc = r.text

  soup = BeautifulSoup(html_doc, "html.parser")

  # pegando a quantidade de paginas, para colocar no range do for
  total_paginas = soup.find("a", class_="btMaisVagas").get("data-total")

  urls = []
  for c in range(int(total_paginas)):
    valores_paginas = f"https://www.vagas.com.br/vagas-de-{keywords}?pagina={c + 1}"
    urls.append(valores_paginas)


  #----------------------------------------------------------
  # FAZENDO SCRAPPING
  total_jobs = []
  for url_list in urls:
    r = requests.get(url_list)
    html_doc = r.text

    soup = BeautifulSoup(html_doc, "html.parser")

    cards = soup.find_all("li", class_="vaga")
    
    # Descrição do trexo
    # vai criar um dicionario e adicionar em uma lista
    for c in cards:
      dict = {
        "title" : c.find("a").get("title").strip(),
        "company" : c.find("span", class_="emprVaga").string.strip(),
        "nivelVaga" : c.find("span", class_="nivelVaga").string.strip(),
        "location" : c.find("span", class_="vaga-local").get_text().strip(),
        "how_old" : c.find("span", class_="data-publicacao").get_text().strip(),
        "link" : f"https://www.vagas.com.br/{c.find('a').get('href')}"
      }
    
      total_jobs.append(dict)
  
    #print(jobs)


  #----------------------------------------------------------
  # PASSANDO PARA UM ARQUIVO CSV
  file = open("total_jobs.csv", "w")

  escrever = csv.writer(file)
  escrever.writerow(["title", "company", "nivelVaga", "location", "how_old", "link"])
  #print(escrever)

  for c in total_jobs:
    print("escrevendo url")
    escrever.writerow(c.values())
