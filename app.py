from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

lista_recados = [
    {"nome": "José", "mensagem": "estudando flask e jinja"},
    {"nome": "Rayssa", "mensagem": "varrendo a casa"},
    {"nome": "Zenaide", "mensagem": "fazendo almoço"}
]

@app.route("/")
def index():
    return render_template("index.html", lista_recados=lista_recados)

@app.route("/novo_recado")
def novo_recado():
    return render_template("novo_recado.html")

@app.route("/adicionar_recado", methods=["POST"])
def adicionar_recado():
    nome = request.form["nome"]
    msg = request.form["msg"]
    lista_recados.append({"nome": nome, "mensagem": msg})
    return redirect(url_for("index"))

@app.route("/recados/<int:id>/editar_recado")
def editar_recado(id):
    recado = lista_recados[id]
    return render_template("editar_recado.html", recado=recado, id=id)

@app.route("/recados/<int:id>/atualizar_recado", methods=["POST"])
def atualizar_recado(id):
    nome = request.form["nome"]
    msg = request.form["msg"]
    lista_recados[id] = {"nome": nome, "mensagem": msg}
    return redirect(url_for("index"))

@app.route("/recados/<int:id>/tela_excluir_recado")
def tela_excluir_recado(id):
    recado = lista_recados[id]
    return render_template("excluir_recado.html", recado=recado, id=id)

@app.route("/recados/<int:id>/excluir_recado")
def excluir_recado(id):
    del lista_recados[id]
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)