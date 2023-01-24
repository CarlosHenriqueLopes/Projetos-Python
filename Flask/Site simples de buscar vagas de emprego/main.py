from flask import Flask, render_template, request, redirect
from wisen import get_jobs


# nome da aplicação
app = Flask("CarlosHenrique")

# rota (/ - index - raiz, (pag inicial))
@app.route('/')
def hello_world():
    return render_template("pagina1.html")

@app.route("/login")
def login():
  return "Páginas de login"

#adicionando parametro (alterar pela url) obs: legal para easter eggs
@app.route('/<user>')
def welcome(user):
  user = f"{user}"
  return render_template("eastereggs.html", user=user)


#-----------------------------
#TEMPLATE
@app.route("/search")
def searc():
  return render_template("search.html")


@app.route("/result")
def result():
  print(request.args) # mostrar o argumentos com o request
  print(request.args.get("variavel")) # mostra o valor digitado na input
  
  keyword = request.args.get("variavel").lower()
  p_h1h2 = keyword.upper()
  
  if keyword: # se for digitado
    pegando_resultados = get_jobs(keyword)
  else:
    return redirect("/")
    
  return render_template("result.html", RefNo_HTML=pegando_resultados, RefNo_HTML2=p_h1h2)

#(flask run para executar de um computador)
app.run(host="0.0.0.0") #-> para o replit