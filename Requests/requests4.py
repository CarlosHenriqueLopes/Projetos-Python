import requests

def main():
  print("Digite um site")
  
  url = str(input(": ->  ")).lower().split(",")
  print()
  
  for c in url:
    url = c.strip()
    print(url)
  
    if "." not in url:
      print(f"A URL {url} está invalida, coloque < . > (ponto)")
      print()
    elif "https" not in url:
        nova_url = f"https://{url}"
  
        try:
          r = requests.get(nova_url)
          
          if r.status_code >= 200 and r.status_code < 300:
            print("[codigo 200] O site está online")
            print()
          elif r.status_code >= 300 and r.status_code < 400:
            print("[codigo 300] redirect")
            print()
          elif r.status_code >= 400 and r.status_code < 500:
            print("[codigo 400] erro do cliente")
            print()
          else:
            r.status_code >= 300 and r.status_code < 600
            print("[codigo 300] erro do servidor")
            print()
        except:
          print(f"Está URL -> {nova_url} está invalida")
          print()
          
  menu()

def menu():
  escolha = str(input("Quer continuar? ")).lower().strip()[0]

  if "s" in escolha:
    main()
  else:
    print("Saindo do programa")

main()