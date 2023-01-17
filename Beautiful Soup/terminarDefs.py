"""
exemplo para o dicionario
jobs = {
  "title": "titulo da vaga",
  "company": "empresa que anuncia a vaga",
  "QtdDVaga": "local da vaga",
  "how_old": "quanto tempo faz que foi cirada"
}
"""

# Fazendo o Scrapping

import requests
from bs4 import BeautifulSoup

#colocar site em uma variavel
site = "https://www.catho.com.br/vagas/?pais_id=31&q=python"
#https://www.catho.com.br/vagas/?pais_id=31&q=python
#https://www.catho.com.br/vagas/python/?q=python&page=2



# fazer a contagem de paginas na def search_keyword()  (terminar)

def search_keyword(keyword):
  r = requests.get(f"https://www.catho.com.br/vagas/python/?q={keyword}&page=2")
  html_doc = r.text

  soup = BeautifulSoup(html_doc, "html.parser")

  pages_links = soup.find("nav", class_="Pagination__Wrapper-sc-1lcjvm4-0 iTxIWl").get("a", {"tabindex" : "0"}).string
  print(pages_links)
'''  for c in pages_links:
    print(c.string)'''

  #print(pages_links)




#----------------------------------------------------------------------
# pegando info das vagas

def scrapping(url):
  
  #fazendo a requisição, pegando arqv texto
  r = requests.get(url)
  html_doc = r.text
  
  soup = BeautifulSoup(html_doc, "html.parser")
  
  cards = soup.find_all("article", class_="Card__CardWrapper-sc-om5cci-0 hqncyC sc-bwCtUz CgSOf")
  
  #print(cards) # -> print de verificação
  
  
  #Para ajudar a localizar os valores
  '''for c in cards:
    print(c.find("a").get_text()) #-> title
    print(c.find("p", class_="sc-esjQYD yKksJ").string) #-> company
    print(c.find("strong").string) #-> QtdDVaga
    print(c.find("time", class_="sc-hrWEMg ixNjRP").get_text()) #-> how_old
    print("------------------")'''
  
  
  # Descrição do trexo
  # vai criar um dicionario e adicionar em uma lista
  jobs = list()
  for c in cards:
    dict = {
      "title" : c.find("a").get_text(),
      "company" : c.find("p", class_="sc-esjQYD yKksJ").string,
      "QtdDVaga" : c.find("strong").string,
      "how_old" : c.find("time", class_="sc-hrWEMg ixNjRP").get_text(),
      "link" : f"https://www.catho.com.br/vagas/{c.find('a').get('href')}"
    }
    
    if dict["company"] == None:
      dict["company"] = "Empresa Confidencial"
      
    jobs.append(dict)

  return jobs

#print(scrapping(site))
search_keyword("python")