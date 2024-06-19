
"""
#questão1
v1 = int(input("Digite um número: "))
v2 = int(input("Digite um número: "))

if v1>v2:
    print(f"O valor {v1} é maior")
elif v1<v2:
    print(f"o valor {v2} é maior")
elif v1==v2:
    print(f"Os valore são iguais")


"""
#questão2
"""

idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 64:
    print(f"Voce é maior de idade")
elif idade < 18:
    print(f"Voce é menor de idade")
elif idade > 65:
    print(f"voce é idoso")

"""
#questão3

"""

login = str(input("Digite seu email:"))
senha = str(input("Digite sua senha:"))
loginCerto = "Lari123"
Senhacerta = "07072007"

if login == loginCerto and senha == Senhacerta:
    print(f"Seu login está certo")
elif login != loginCerto and senha != Senhacerta:
    print(f"seu login está errado")

"""

#questão4

"""

peso = float(input("Digite seu peso(em kg):"))
altura = float(input("Digite sua altura(em metros):"))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Abaixo do peso")
elif imc >= 18.6 and imc <= 24.9:
    print(f"Peso normal")
elif imc >= 25 and imc <=29.9:
    print(f"Sobrepeso")
elif imc >= 30:
    print(f"Obesidade")


"""

#Questão5

"""

import random
n_secreto = random.randint(1,10)
chute = int(input("Adivinhe um número entre 1 e 10: "))
print(n_secreto)
if chute == n_secreto:
    print("Acertouuu!!")
else:
    print("Errouuuu!!")

"""

"""
 #questão6 -


letra =input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("a letra é uma vogal.")
elif letra.isalpha():
    print("a letra é uma consoante")
else:
    print("Entrada inválida. Digite uma letra.")

"""

#Questão7
"""

valorCompra = float(input("Qual o valor da sua compra? "))
formaDepagamento = str(input("Qual a forma de pagamento?"))

if formaDepagamento == "pix" or formaDepagamento == "dinheiro":
    desconto = (valorCompra * 0.15)
    print(f"")
elif formaDepagamento == "boleto":
    desconto2 = (valorCompra * 0.10)
elif formaDepagamento == "cartão":
    desconto3 = (valorCompra * 0.05)
elif formaDepagamento == "cartão":
    desconto4 = (valorCompra * 0.03)

"""

import random
opcoes = ["pedra", "papel", "tesoura"]
escolha = input("Escolha: pedra, papel ou tesoura:").lower()
chute =  random.choice(opcoes)
print(chute)
if escolha == chute:
    print("Empate!")
elif (escolha == "pedra" and chute =="tesoura") or \
     (escolha == "papel" and chute =="pedra") or  \
     (escolha == "tesoura" and chute =="papel") or \
     print("Voce venceu!!")
else:
    print("Voce perdeu!!")










