'''
Vai mostrar as vagas da primeira pagina, com as descrições do for
'''


import requests
from bs4 import BeautifulSoup

# -> site usado https://www.vagas.com.br

def scrapping(job):

  r = requests.get(f"https://www.vagas.com.br/vagas-de-{job}?")
  html_doc = r.text

  soup = BeautifulSoup(html_doc, "html.parser")

  cards = soup.find_all("li", class_="vaga")

  # Descrição do trexo
  # vai criar um dicionario e adicionar em uma lista
  jobs = list()

  for c in cards:
    dict = {
        "title" : c.find("a").get("title"),
        "company" : c.find("span", class_="emprVaga").string,
        "nivelVaga" : c.find("span", class_="nivelVaga").string,
        "location" : c.find("span", class_="vaga-local").get_text(),
        "how_old" : c.find("span", class_="data-publicacao").get_text(),
        "link" : f"https://www.vagas.com.br/{c.find('a').get('href')}"
    }

    jobs.append(dict)

  print(jobs)
## Fazer opção para filtrar as titulos, company etc...