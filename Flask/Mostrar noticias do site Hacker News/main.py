"""
Link: https://news.ycombinator.com/
Hacker News é um site de notícias sociais com foco em ciências da
computação e empreendedorismo.

O programa vai pegar umas APIs dele e criar uma aplicação web para listar
notícias do site.
"""


from flask import Flask, render_template, request, redirect
import requests

app = Flask("CarlosHenrique")

# URL que lista as noticias mais recentes:
# https://hn.algolia.com/api/v1/search_by_date?tags=story

# URL que lista as noticias/conversas mais populares: (def home())
# https://hn.algolia.com/api/v1/search?tags=story

# URL que traz mais informações de uma noticia passando o ID dela:
# https://hn.algolia.com/api/v1/items/{id}


@app.route("/")
def home():
  order_by = request.args.get("var") # Lembrete davariavel ?var=
  
  if order_by == "news":
    url = "https://hn.algolia.com/api/v1/search_by_date?tags=story" #->noticias mais recentes
    
  else:
    url = "https://hn.algolia.com/api/v1/search?tags=story" #->noticias/conversas mais populares
  
  res = requests.get(url).json()["hits"] #->pegando os dados a url, passando para json e pegando a key hits
  return render_template("index.html", res_html=res, order=order_by)

  
#----------------------------------------------------------------
# informações de uma noticia passando o ID dela
  
@app.route("/<id>")#->p/quando for digitado qualquer coisa, no caso o id lá no html
def id_noticias(id):
  # OBS: Essa url está com o id da função que é o valor do route, que é uma rariavel da url
  #que estou passando pelo html, pegando .objectID do requests.get(url).json()["hits"]
  url = f"https://hn.algolia.com/api/v1/items/{id}"
  res = requests.get(url).json()
  return render_template("ids.html", res_html=res)

  
app.run(host="0.0.0.0")