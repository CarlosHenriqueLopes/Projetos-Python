import requests
from bs4 import BeautifulSoup
import csv

#colocar site em uma variavel
site = "https://www.vagas.com.br/vagas-de-python"

#fazendo a requisição, pegando arqv texto
r = requests.get(site)
html_doc = r.text

soup = BeautifulSoup(html_doc, "html.parser")

cards = soup.find_all("li", class_="vaga")

jobs = list()

for c in cards:
  dict = {
    "title" : c.find("a").text.strip(),
    "company" : c.find("span", class_="emprVaga").string.strip(),
    "nivelVaga" : c.find("span", class_="nivelVaga").string.strip(),
    "location" : c.find("span", class_="vaga-local").get_text().strip(),
    "how_old" : c.find("span", class_="data-publicacao").get_text().strip(),
    "link" : f"https://www.vagas.com.br/{c.find('a').get('href')}"
  }

  jobs.append(dict)

  

#------------------------------------------------------------
  
#fazendo o csv das vagas encontradas em uma pagina
# w write (overwrite subescreve), usando pq so vou usar uma vez
file = open("jobs.csv", "w")

write = csv.writer(file)
# adicionando manualmente os titulos para a tabela (sao as keys do dict da lista)
write.writerow(["title", "company", "nivelVaga", "location", "how_old", "link"])

# adicionando os valores da lista
for c in jobs:
  write.writerow(list(c.values()))