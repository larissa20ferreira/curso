from flask import render_template, Flask
import pandas as pd 
app = Flask(__name__)

class Livro:
    def __init__(self, titulo, autor, categoria, ano, editora):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.editora = editora
        self.ativo = False

@app.route("/inicio")
def home():
    df = pd.read_csv("tabela - livros.csv")
    lista_de_livros = []
    for index, row in df.iterrows():
        livro = Livro(
            row["Titulo do Livro"],
            row["Autor"],
            row["Categoria"],
            row["Ano de Publicação"],
        )
        lista_de_livros.append(livro)
    lista = df["Titulo do Livro"].tolist()
    return render_template("lista.html", titulo=TITULO, lista_de_livros=lista_de_livros)



@app.route("/inicio")
def ola():
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 1954, "HarperCollins")
    lista = ["O Senhor dos Anéis", "Dom Casmurro", "O Alquimista"]
    livro2 = Livro("Dom Casmurro", "Machado de Assis", "Romance", 1899, "Martin Claret")
    livro3 = Livro("O Alquimista", "Paulo Coelho", "Autoajuda", 1988, "Rocco")
    lista = [livro1, livro2, livro3]

    return render_template(
        "lista.html", titulo="Listagem de Livros - SENAI", lista_de_livros=lista
    )

app.run()
