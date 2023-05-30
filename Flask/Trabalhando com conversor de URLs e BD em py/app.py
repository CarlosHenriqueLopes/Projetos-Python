from flask import Flask, abort
from bd import users
from converters import ListConverter

app = Flask(__name__)
#OBS: o msm nome que eu chamar nesta lista, é o msm que coloca quando chama
# app.url_map.converters["regex"] = RegexConverter
app.url_map.converters["list"] = ListConverter


## Home page: mostra do nomes das pessoas que estão no BD pelo link
@app.route("/")
def index():
    lista_html = ["<ul>"]
    for k, v, in users.items():
        lista_html.append(f"<li><a href='/user/{k}' -> {v['name']}</a></li>")
    lista_html.append("</ul>")

    return "\n".join(lista_html) #-> a cada quebra de linha ajunta a lista


## O list foi criado como conversor de url para mostrar mais usuários na página
##usando somar. Ex: /user/nome1+nome2...
@app.route("/user/<list:variaveis>")
def profile(variaveis):
    html = " "
    for variavel in set(variaveis): #set() -> elimina duplicidaes (caso a pessoa digite os msm valores)
        #user está armazenando o BD, que esta dando um get no valor digitado, que vai ser uma key do BD
        user = users.get(variavel)

        #se user for verdadeiro, retorna um html com o bd da variável
        if user:
            html += f"""
                <h2>{user['name']}</h2>
                Telefone: {user['tel']} <br><br>
                <a href='/'>Voltar para home</a>
                <hr>
                """

    return html or abort(404, "Este nome não está no banco de dados")


## O int no parametro, é um conversor de url
@app.route("/user/<variavel>/<int:variavel2>")
def quote(variavel, variavel2):
    userdb = users.get(variavel)
    quote = userdb.get("quotes").get(variavel2)

    if userdb and quote:
        return f"""
            <h2>Descrição: {userdb['name']}</h2>
            <p><q>{quote}</q></p><br><br>
            <a href="/">Home page</a>
            """
    else:
        return abort(404, "ID não encontrado")


# com o conversor de url path, ilimitados caminhos/pastas
# ex: /file/pasta1/pasta2/arquivo.jpg
@app.route("/file/<path:variavel>")
def file(variavel):
    return f"exemplo para mostar os carminho: {variavel}"


'''# o conversor de url regex() aceitar determinadas variaveis, no caso começando com <A> e pode vim qualquer coisa depois
@app.route("/reg/<regex(a.*):variavel>")
def reg1(variavel):
    return f"Qualquer argumento iniciando com a letra a: {variavel}"

@app.route("/reg/<regex:(b.*)variavel>")
def reg1(variavel):
    return f"Qualquer argumento iniciando com a letra b: {variavel}"'''

app.run(use_reloader=True)