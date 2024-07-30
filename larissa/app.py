from flask import Flask , render_template

app = Flask(__name__)
TITULO= "lista de livro - senai"

@app.route("/inicio")
def ola():
    livro = "Senhor dos Aneis"
    lista_de_livros = ["Senhor dos Aneis", "Don Casmuro", "Codigo Limpo"]
    return render_template("lista.html",titulo=TITULO, livro1=livro)

app.run(debug=True)