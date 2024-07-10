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
    x = input("Digite um número (ou 'fim' para sair): ")
    if x.lower() == "fim":
        break
    numeros.append(float(x)) 
    print(numeros)
media = sum(numeros)  / len(numeros)
print("Média: ",media)
"""

"""
#Questão06

soma_impares = 0
for num in range(1, 101):
    if num % 2 != 0:
        soma_impares += num
print("A soma de todos os números ímpares de 1 até 100 é:", soma_impares)

"""
"""

#Questão07
import random
n = random.randint(1,100)
#print(n)

while True:
    chute = int(input("Informe um número: "))
    if chute < n:
        print("{} é menor".format(chute))
    elif chute > n:
        print("{} é maior".format(chute))
    else:
        print("Acertou!!!")
        break

"""

"""
#Questão08

string = input("Digite uma string: ")
vogais = "aeiouAEIOU"
num_vogais = 0
for char in string:
    if char in vogais:
        num_vogais += 1
print(f"O número de vogais na string '{string}' é: {num_vogais}")

"""
"""

#Questão09
while True:
    operando1 = float(input("Digite o primeiro operando (ou 0 para sair): "))
    operando2 = float(input("Digite o segundo operando (ou 0 para sair): "))
    if operando1 == 0 and operando2 == 0:
        print("Encerrando a calculadora...")
        break
    print("Escolha uma operação:")
    print("1 - Soma")
    print("2 - Produto")
    print("3 - Divisão")
    print("4 - Potência")
    escolha = int(input("Digite o número da operação desejada: "))
    if escolha == 1:
        resultado = operando1 + operando2
        print(f"Resultado da soma: {resultado}")
    elif escolha == 2:
        resultado = operando1 * operando2
        print(f"Resultado do produto: {resultado}")
    elif escolha == 3:
        if operando2 != 0:
            resultado = operando1 / operando2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Não é possível dividir por zero. Tente novamente.")
    elif escolha == 4:
        resultado = operando1 ** operando2
        print(f"Resultado da potência: {resultado}")
    else:
        print("Escolha inválida. Tente novamente.")
    
    print() 
print("Obrigado por usar a calculadora!")



"""