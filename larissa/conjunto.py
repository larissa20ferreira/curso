"""
conjunto = {1,1,1,1,1,2,3,4,5,6,7}
#não mostra números repetidos
print(conjunto)
#cria um conjunto vazio
meu_conjunto = set()
print(meu_conjunto)

#remover item do conjunto
conjunto.remove(2)
print(conjunto)

#Verificando um elemento
meu_conjunto = {7,8,9}
print("Tem o 7 no conjunto: ", 7 in meu_conjunto) #retorna verdadeiro
print("Tem o 10 no conjunto: ", 10 in meu_conjunto) #retorna falso

#Operação conjunto - UNIÃO
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
uniao = conjunto01 | conjunto02
print("União do 1 com o 2: ", uniao)

#Operação conjunto - INTERSECAO
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
intersecao = conjunto01 & conjunto02
print("Interseção do 1 com o 2: ", intersecao)

#Difereça
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
diferenca = conjunto01 - conjunto02
print("A diferença (o que está no conjunto 1): ", diferenca)

#Diferenca Simétrica
conjunto01 = {1,2,3}
conjunto02 = {3,4,5}
simetrica = conjunto01 - conjunto02
print("Diferença (o que não tem em comum): ", simetrica)


conjunto = {1,1,1,1,1,2,3,4,5,6,7}
conjunto.clear()
print(conjunto)

"""













