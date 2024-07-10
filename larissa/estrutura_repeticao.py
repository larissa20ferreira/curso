"""

range(0,10,)
list(range(0,10,1))

for i in  range (10):
    print(i)
    print("olá")

palavra = "diego"
for i in palavra:
    print(i)
"""

"""

for i in range(100):
    if i %2==0:
        print("{} é par".format(i))

"""
"""
#QuestãoExemplo#
nome = (input("informe um nome:" ))
for i in range(len(nome)+1):
    print(nome[:i])

"""
"""
#QuestãoExemplo
y = 10
while y >= 5:
    print(y)
    #y = y - i
    y -= 1

"""
"""

#Questão01
for i in range(10,0, -1):
    print(i)
"""
"""

#Questão02
n = int(input("Informe um número: "))
for i in range (1,11):
    print(f"{n} x {i} = {n*i}")
"""

"""

#Questão03
valor = int(input("Informe um número: "))
fatorial = 1
for i in range(1, valor +1 ): 
    fatorial *=i 
    print(f"o variavel fatorial é {fatorial}")
    
"""
"""
#Questão04

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))
if x < y:
    for num in range(x, y + 1):
        print(num, end=" ")
else:
    for num in range(y, x + 1):
        print(num, end=" ")
print()

"""
"""
#Questão05

numeros = []
while True:
    entrada = input("Digite um número (ou 'fim' para encerrar): ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = float(entrada) 
        numeros.append(numero)
    except ValueError:
        print("Por favor, digite um número válido ou 'fim' para encerrar.")
if len(numeros) > 0:
    media = sum(numeros) / len(numeros)
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número foi digitado para calcular a média.")

"""