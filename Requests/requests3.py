import requests
import sys  # Lembrete: para passar o argumento na frente

status_on = [200, 303, 304, 302, 301]

# argv[1] para pegar o 1º argumento (pegar o valor do usuario)
site = str(sys.argv[1])

# Verificar se tem ponto <.>
if "." not in site:
    print("URL invalida.\nAdicione ponto <.> na sua URL")

else:
    if "http" not in site:
        # caso não tenha digitado o http
        site = f"https://{site}"

        try:
            # se digitado, fazer o request (pegar o site)
            r = requests.get(site)
            # verificação do status code
            status = r.status_code
            if status in status_on:
                print("online")
                maquina = input(str("Entrar no site? [s/n]")).upper().strip()[0]
                if maquina == "S":
                    print(site)
                else:
                    print("OBG por testar")
            else:
                print("offline")
        except:
            print("site invalido")