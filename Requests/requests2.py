"""
Web Scraper:
vai varrer varios sites e depois organizar os dados
mostrando a condição pelo status code
"""

import requests

site = "https://www.google.com/abcde"
r = requests.get(site)

if r.status_code >= 200 and r.status_code < 300:
  print("O site está online")
elif r.status_code >= 300 and r.status_code < 400:
  print("redirect")
elif r.status_code >= 400 and r.status_code < 500:
  print("erro do cliente")
elif r.status_code >= 300 and r.status_code < 600:
  print("erro do servidor")
