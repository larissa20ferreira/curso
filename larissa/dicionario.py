# exemplo
"""
lucro_total = 0
for mes, lucro in total.intens():
    lucro_total += lucro
    if lucro > 2000:
        print(mes)
print(lucro_total)
novo_total2 = sum(novo_total2)
print(novo_total2)

"""


#exemplo
#converter o valor dos produtos de dolar para real
"""
valor_dolar = {
    'produtoA': 0.75,
    'produtoB': 4.75,
    'produtoC': 3.35
}
print(valor_dolar)
conversão = 5.70
valor_real = {
    chave : round(valor * conversão, 2)
    for chave, valor in valor_dolar.items()
}
print("Valor em R$:", valor_real )

"""
"""
#atividade01
aluno = {
    'nome' : 'larissa',
    'idade' : '17 anos',
    'curso' : 'python'
}
print(aluno['nome'])

"""
"""
#atividade02

aluno = {
    'nome' : 'larissa',
    'idade' : '17 anos',
    'curso' : 'python'
}
aluno ['idade'] = 21
aluno.update('nota' : 9.5)
print(aluno['nome'])
print(aluno['idade'])
print(aluno['nota'])
print(aluno['curso'])

"""
"""

#atividade03
aluno = {
    'nome' : 'larissa',
    'idade' : '17 anos',
    'curso' : 'python'
}
aluno.update('nota' : 9.5)
print(aluno)
aluno ['idade'] = 21
print(aluno)
for chave, valor in aluno.items():
    print(f"{chave} : {valor}")
if 'nomes' in aluno:
    print("A chave está presente")
else:
    print("A chave nome NÃo está presente")
"""
#atividade4
"""
#criam dois dicionário
d1 = {'a':10, 'b':20, 'c':30}
d2 = {'c':50, 'd':15, 'e':30}
print(d1)
print(d2)
for chave, valor in d2.items(): #itera sobre o dicionário
    if chave in d1: #verifica se a chve está no d1
        d1[chave] = d1[chave] + valor #se sim pega o valor e soma o novo valor
        print("A soma do valor repetido é:",d1[chave]) # imprime o resultado
    else: 
       print("Não tem chave repetida") #caso não tenha imprime e d1 e o d2
       break 

"""
"""
info = {
    'aluno1':{'nome': 'Joao', 'idade':'20', 'nota':'8.0'},
    'aluno2':{'nome': 'Maria', 'idade':'18', 'nota':'9.0'},
    'aluno3':{'nome': 'Miguel', 'idade':'22', 'nota':'7.0'}
}
print(info)
#fazer a média das notas
soma_nota = 0
for aluno in info.values():#itera sobre os valores do dicionário
    soma_nota += aluno['nota'] #acumula o valor das notas
media = soma_nota/len(info) #divide as notas pelos tamanhos do dicionário
print("A média dos alunos é", media)
"""
#outro exemplo

"""info = {
    'aluno1':{'nome': 'Joao', 'idade':'20', 'nota1':'8.0', 'nota1':'6.0', 'nota1' :'4.0'},
    'aluno2':{'nome': 'Maria', 'idade':'18', 'nota1':'9.0', 'nota1':'7.0', 'nota1':'8.0'},
    'aluno3':{'nome': 'Miguel', 'idade':'22', 'nota1':'7.0' 'nota1' :'9.0', 'nota1':'2.0'}
}
print(info)
#fazer a média das notas
soma_nota = 0
for aluno in info.items():#itera sobre os valores do dicionário
    media = (notas['n1'] + notas['n2']+['n3'])/3
    print(f"A média de {aluno} é: {media:2f}")
    if media > 8.0:
        alunos_aprovados.update(aluno)"""

   














