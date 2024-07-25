import pandas as pd 
"""
df = pd.read_csv("tabela_livros.csv")

print(df)"""

class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo

livro = Livro("Codigo Limpo", "Julio", "Programação", 2012, "Sim")
livro1 = Livro("Codigo Limpo 1", "Larissa", "Programação", 2012, "Sim")
livro2 = Livro("Codigo Limpo 2", "Ellen", "Programação", 2012, "Sim")
print(livro.autor)
print(livro1.autor)
print(livro2.autor)
lista_de_livros = [livro, livro1, livro2]

for livro in lista_de_livros:
    print(livro.titulo)