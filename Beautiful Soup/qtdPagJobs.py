"""
Vai fazer um scrapping e contar a quantidade de paginas por jobs procurados
"""

# OBS Só para estudo
# Cod do site foi mudado

import requests
from bs4 import BeautifulSoup
import math

url_base = 'https://br.indeed.com/empregos?'

# keyword -> colocar o job
def search_keyword(keyword):
  #url + request
  r_indeed = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  html_indeed = r_indeed.text
  #make a soup
  soup = BeautifulSoup(html_indeed, 'html.parser')
  
  #pega numero de resultados de vagas
  total_jobs = soup.find('div', id='searchCountPages').text

  
  tmp_list = total_jobs.strip().split(' ')
  #print(tmp_list) # -> lista separada por espaços
  
  total_number = int(tmp_list[3].replace('.', ''))
  #-> terceiro valor da lista, tirando o ponto e deixando em formato int
  #print(total_number)
  
  pages_to_scrap = math.ceil(total_number/50) #-> meth.ceil arredondar o valor

  return pages_to_scrap

print(search_keyword("python"))
