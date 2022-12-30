import requests

url = "https://www.bbc.co.uk/"
site = requests.get(url)

lista = ["admin", "login", "css", "sport"]

#print(site.text) #-> para mostrar o codigo font .text

#print(site.status_code) # 200, 404...

for c in lista:
    url_lista = url + c
    print(url_lista) # mostra os links

    r = requests.get(url_lista) # armazenar os links
    print(r.status_code) # mostrar os status codes


for c in lista:
    url_lista = url + c

    r = requests.get(url_lista)

    if r.status_code == 200:
        print(url_lista)
        print(r.status_code)
        print("---------------")
        #print(f"Links com cogido 200 {url_lista} - cod:{r.status_code}")
    else:
        print(url_lista)
        print(r.status_code)
        print("----------------")
        #print(f"links com codigo != de 200 {url_lista} - cod:{r.status_code}")
#----------------------------------------------------------------------------------------------------------------


# Para DNSs

url = "terra.com.br"

lista = ["admin", "login", "css", "sport", "mail", "painel", "central"]

for c in lista:
    sub_to_check = f"https://{c}.{url}"

    try:
      r = requests.get(sub_to_check)
      print()
      print("acesso ok")
      print(sub_to_check)
    except:
      print()
      print("não foi possivel acessar")
      print(sub_to_check)
      continue