import requests
from bs4 import BeautifulSoup

site = "https://www.iban.com/currency-codes"

requisicao = requests.get(site)
html_doc = requisicao.text

soup = BeautifulSoup(html_doc, "html.parser")
tab = soup.find("table")
body = tab.find("tbody")
linhas = body.find_all("tr")# -> organizando as linhas em uma lista

pack = list()
for c in linhas:
  itens = c.find_all("td")
  pais = itens[0].text
  moeda = itens[1].text
  code = itens[2].text
  #valor = itens[3].text


  """
  Filtro para paises que nao possuem moeda universal,
  depois colocando em um dicionario, para adicionar em uma lista
  """
  if "No universal currency" not in moeda:
    paises = {
      "nome_pais" : pais,
      "code_moeda" : code
    }
    
  pack.append(paises)
  
"""
# Referencia
print(pack[0])
print(pack[0]["nome_pais"])
print(pack[0]["code_moeda"])
print()
"""

def menu():
  tm_lista = len(pack)
  
  try:
    escolha = int(input(f"Escolha um número de 1 a {tm_lista}: ")) -1
    print()
    if escolha > tm_lista:
      print("-Esse número não está na lista-\n")
      menu()
    else:
      print(f"você escolheu o país {pack[escolha]['nome_pais']} e o codigo da moeda é {pack[escolha]['code_moeda']}\n")
      
      continuar = str(input("Deseja ver outro país? ")).lower().strip()[0]
      if "s" in continuar:
        menu()
      else:
        print("\nSeja feliz!")
      
  except ValueError:
    print("\n-Não digite por extenso-\n")
    menu()


print("CÓDIGOS DE MOEDA DE PAÍSES")
for p, c in enumerate(pack):
  print(f"{p +1} - {c['nome_pais']}")

print()
menu()