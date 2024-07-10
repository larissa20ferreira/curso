
"""
#questão1
v1 = int(input("Digite um número: "))
v2 = int(input("Digite um número: "))
se v1>v2:
    print(f"O valor {v1} é maior")
Elif v1<v2:
    print(f"o valor {v2} é maior")
Elif v1==v2:
    print(f"Os valores são iguais")
"""
#questão2
"""
idade = int(input("Digite sua idade: "))
se idade >= 18 e idade < 64:
    print(f"Você é maior de idade")
Idade menor < 18:
    print(f"Você é menor de idade")
Idade > 65 anos:
    print(f"você é idoso")
"""
#questão3

"""
login = str(input("Digite seu email:"))
senha = str(input("Digite sua senha:"))
loginCerto = "Lari123"
Senhacerta = "07072007"
if login == loginCerto e senha == Senha certa:
    print(f"Seu login está correto")
elif login != loginCerto e senha != Senha certa:
    print(f"seu login está errado")
"""

#questão4

"""
peso = float(input("Digite seu peso(em kg):"))
altura = float(input("Digite sua altura(em metros):"))
imc = peso / (altura ** 2)
se imc < 18,5:
    print(f"Abaixo do peso")
elif imc >= 18,6 e imc <= 24,9:
    print(f"Peso normal")
elif imc >= 25 e imc <=29,9:
    print(f"Sobrepeso")
elif imc >= 30:
    print(f"Obesidade")
"""

#Questão5

"""
importar aleatoriamente
n_secreto = random.randint(1,10)
chute = int(input("Adivinhou um número entre 1 e 10: "))
imprimir(n_secreto)
if rampa == n_secreto:
    print("Acertouuu!!")
outro:
    print("Errouuu!!")
"""

"""
#questão6 -
letra =input("Digite uma letra: ").lower()
if letra em "aeiou":
    print("a letra é uma vogal.")
elif letra.isalpha():
    print("a letra é uma consoante")
outro:
    print("Entrada inválida. Digite uma letra.")
"""

#Questão7
"""

valorCompra = float(input("Qual o valor da sua compra? "))
print("Qual a forma de pagamento:")
print("--------------------------")
print("1-pix, 2-boleto, 3-parcelado cartão")
forma = int(input())

if forma == 1:
    desconto = valorCompra * 0.15
    v1_liquido = valorCompra - desconto
elif forma == 2:
    desconto = valorCompra * 0.10
    v1_liquido = valorCompra - desconto
elif forma == 3:
    parcela = int(input("Informe a quantidade de parcelas: "))
    if parcela <=6:
        desconto = valorCompra * 0.05 
        v1_liquido = valorCompra - desconto
    else:
        desconto = valorCompra * 0.03
        v1_liquido = valorCompra - desconto
print("valor total da compra R$ {}".format(valorCompra))
print("Valor do desconto R$ {}".format(desconto))
print("Valor final da compra R$ {}".format(v1_liquido))

"""

"""
importar  aleatoriamente
opcoes  = [ "pedra" , "papel" , "tesoura" ]
escolha  =  input ( "Escolha: pedra, papel ou tesoura:" ). mais baixo ()
rampa  =   aleatório . escolha ( opcoes )
imprimir ( chute )
if  escolha  ==  rampa :
    print ( "Empate!" )
elif ( escolha  ==  "pedra"  e  chute  == "tesoura" ) ou \
     ( escolha  ==  "papel"  e  rampa  == "pedra" ) ou    \
     ( escolha  ==  "tesoura"  e  chute  == "papel" ) ou \
     print ( "Você venceu!!" )
outro :
    print ( "Você perdeu!!" )

"""   