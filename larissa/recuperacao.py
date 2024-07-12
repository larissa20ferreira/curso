pessoas = []
while True:
    nome = input("Digite o nome(ou 'sair' para encerrar o programa): ")
    if nome.lower() == 'sair':
        break
    idade = int(input("Digite a idade: "))
    if idade < 18:
        classificado = "Criança"
    elif idade >= 18 and idade <= 64:
        classificado = "Adulto"
    else:
        classificado = "Idoso"
    pessoa = {"nome": nome, "idade": idade, "classificacao": classificado}
    pessoas.append(pessoa)
total_pessoas = len(pessoas)
if total_pessoas > 0:
    soma_idades = sum(pessoa['idade'] for pessoa in pessoas)
    idade_media = soma_idades / total_pessoas
else:
    idade_media = 0
for pessoa in pessoas:
    print("==========================================================================")
    print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Classificação: {pessoa['classificacao']}")
print("===========================================================================")
print(f"Pessoas entrevistadas: {total_pessoas}")
print(f"Média: {idade_media}")