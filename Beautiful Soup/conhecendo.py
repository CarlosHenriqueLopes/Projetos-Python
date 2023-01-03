"""
Beautiful Soup:
análise de conteudo html
vai criar uma lista com todos os elementos
Para: instalar bs4
"""
# Documentação https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup

site = "https://www.youtube.com/watch?v=dmsIMntKLhw"
r = requests.get(site)
r_texto = r.text

# pegando o texto html
html_doc = r_texto
# function BeautifulSoup()
soup = BeautifulSoup(html_doc, "html.parser")# html.parser -> processo de linkar, organizar os codigos

print(soup.title)
print()
print(soup.title.name)
print()

# para fazer buscas, find ou find_all obs: são colocados em uma lista
links = soup.find_all("a")
#print(links)

# correndo a lista com for, e pegando os href nela
for c in links:
  print(soup.get("href")) # get para pegar

print(soup.get_text())