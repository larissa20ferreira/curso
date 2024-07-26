import pandas as pd 

df = pd.read_csv("tabela_livros.csv")
print(df)

livro_novo = {
    "Título do livro": ["Python para todos"],
    "Autor": ["Charles Severance"],
    "Categoria": ["Programação"],
    "Ano de Publicação": [2016],
    "Ativo": [True]
}
#Exercício 1
df = df.append(livro_novo, ignore_index=True)

#Exercício 2

livros_programacao = df[df["Categoria"]== "Progranming"]
print("Exercício 2")
print("Livros de programação", livros_programacao)


#Exercí














#df_filtrado = df[df["Ano de Publicação"] == 1993]



## 







"""class Livro:
    def __init__(self, titulo, autor, categoria, ano, ativo):
        self.titulo = titulo
        self.categoria = categoria
        self.ano = ano
        self.ativo = ativo
        self.autor = autor

livro0 = Livro("Livro 0", "Julio", "Progração",2012, "Sim")
livro1 = Livro("Livro 1", "Julio", "Progração",2012, "Sim")
livro2 = Livro("Livro 2", "Julio", "Progração",2012, "Sim")
lista_de_livros = [livro0, livro1, livro2]

for livro in lista_de_livros:
    print(livro.titulo)"""



