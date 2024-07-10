"""
def minha_funcao():
    produto = input ("Informe o nome do produto:").upper()
    #produto = produto.upper()
    print(f"Produto {produto} cadastrado!")
    print("Produto {} cadastrado!".format(produto))


minha_funcao()

"""
"""
def soma(a,b,c):
    return a + b + c 

calculo = soma(10, 20, 0)
print(" Diego ", "está falando de função", calculo)

"""

"""
def minha_funcao():
    produto = input ("Informe o nome do produto:").upper()
    #produto = produto.upper()
    print(f"Produto {produto} cadastrado!")
    print("Produto {} cadastrado!".format(produto))


minha_funcao()

"""
"""
def soma(a,b,c):
    return a + b + c 

calculo = soma(10, 20, 0)
print(" Diego ", "está falando de função", calculo)

"""

#exemplo simples
"""
def saudacao():
    print("Olá, mundo!!!")
saudacao()

#exemplo02
def saudacao(nome):
    print(f"Olá, {nome}")
saudacao()
"""
"""
#exemplo03

def saudacao(nome):
    print(f"Olá, {nome}")
x = input("Digite um nome: ")
saudacao(x)
"""

#exemplo com 2 parametro
"""
def soma(a,b):
    resultado = a + b 
    return resultado
print(" o resultado da soma: ", soma(2,2))
"""
"""
#exemplo 
def soma(a,b):
    resultado = a + b 
    return resultado

n1 = int(input("Digite um némero: "))
n2 = int(input("Digite outro némero: "))
print(f"O resultado da soma de {n1} + {n2} =",soma(n1,n2))

"""
"""def adicao(a,b):
    return a + b 

def subtracao(a,b):
    return a - b 

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    if b != 0:
        return a / b
    else:
        print("Erro: divisão por zero")

def menu():
    print("Escolha uma operação:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    escolha = int(input("Escolha a opção: (1,2,3,4): "))

    n1 = float(input("Digite um número -  "))
    n2 = float(input("Digite outro número -  "))

    if escolha == 1:
        print("Resultado adição:", adicao(n1,n2))
    elif escolha == 2:
        print("Resultado subtração :", subtracao(n1,n2))
    elif escolha == 3:
        print("Resultado divisão:", divisao(n1,n2))
    elif escolha == 4:
        print("Resultado multiplicação:", multiplicacao(n1,n2))

menu()"""



#analise da vendas 
"""vendas = {1200, 850,950, 700,1100,900,1200,1000,850,900,950,900}
def TotalVendas(vendas):
    return sum(vendas)

def MediaVendas(vendas):
    return round(sum(vendas)/len(vendas),2)

def MelhorMes(vendas):
    return vendas.index(max(vendas))+ 1

def PiorMes(vendas):
    return vendas.index(min(vendas))+ 1

print("Total de vendas: ", TotalVendas(vendas))
print("Média de vendas: ", MediaVendas(vendas))
print("Melhor mes de vendas: ", MelhorMes(vendas))
print("Pior de vendas: ", PiorMes(vendas))"""

#Atividade 02

"""def contar_palavra(texto): 
    palavra = texto.split('. ') 
    return len(palavra)
def contar_letras(texto):
    return len(texto)

def contar_frases(texto):
    frase = texto.split('.') 
    return len(frase)

text = str(input("Digite um texto: "))
print("Quantidade de palavras: ", contar_palavra(text))
print("Quantidade de letras: ", contar_letras(text))
print("Quantidade de frases: ", contar_frases(text))"""



#Atividade 03