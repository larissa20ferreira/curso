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
pessoas = []
while True:
    nome = input("Digite o nome da pessoa (ou 'sair' para finalizar): ")
    if nome.lower() == 'sair':
        break
    try:
        idade = int(input("Digite a idade da pessoa: "))
    except ValueError:
        print("Idade inválida, tente novamente.")
        continue

    if idade < 18:
        classificacao = 'Criança'
    elif 18 <= idade < 65:
        classificacao = 'Adulto'
    else:
        classificacao = 'Idoso'
    
    pessoa = {"nome": nome, "idade": idade, "classificacao": classificacao}
    pessoas.append(pessoa)

total_pessoas = len(pessoas)
if total_pessoas > 0:
    soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
    idade_media = soma_idades / total_pessoas
else:
    idade_media = 0

print("\nDados das pessoas entrevistadas:")
for pessoa in pessoas:
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Classificação: {pessoa['classificacao']}")
    
print(f"\nNúmero total de pessoas entrevistadas: {total_pessoas}")
print(f"Idade média das pessoas entrevistadas: {idade_media:.2f}")











