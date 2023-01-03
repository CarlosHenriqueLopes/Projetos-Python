"""
exemplo para o dicionario
jobs = {
  "title": "titulo da vaga",
  "company": "empresa que anuncia a vaga",
  "location": "local da vaga",
  "how_old": "quanto tempo faz que foi cirada"
}
"""
# Documentação https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# Fazendo o Scrapping

import requests
from bs4 import BeautifulSoup

#colocar site em uma variavel
site = "https://www.vagas.com.br/vagas-de-python"

#fazendo a requisição, pegando arqv texto
r = requests.get(site)
html_doc = r.text

soup = BeautifulSoup(html_doc, "html.parser")

cards = soup.find_all("li", class_="vaga")

#print(cards) # -> print de verificação

"""
1º p/facilitar montar um looping for antes de passar para o dicionario

for c in cards:
  print(c.find("a").get("title"))
  #obs: no caso de substituição do .sintr, .get_text() p/ todo valor de texto dentro de uma tag
  print(c.find("span", class_="emprVaga").string)
  print(c.find("span", class_="nivelVaga").string)
  print(c.find("span", class_="vaga-local").get_text())
  print(c.find("span", class_="data-publicacao").get_text())
  print(c.find("a").get("href"))
  print("------------------")
"""

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

print(jobs[0:5])