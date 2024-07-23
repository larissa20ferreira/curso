"""import pandas as pd

#funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';')

#para instalar a biblioteca
#pip install pandas


#Criando Series
s = pd.Series([1,3,5,7,9])
print(s)
#Criando uma data frame
data = {
    'nome':['Ana'],
    'idade':[23,30,35],
    'cidade': ['Pato Branco', 'Vitorino', 'Mariopolis']
    }
df = pd.DataFrame(data)
print(df)

#Exibir primeiras linhas do data frame
print(df.head())
#Exibir as ultimas linhas do data frame
print(df.tail())
#Exibir as informaçõs gerais
print(df.info())
#Descrições as estátisticas
print(df.describe())
#exibir uma coluna
print(df['nome'])
#Exibir multiplas colunas



#Leitura de arquivos 
#Arquivo CSV
funcionarios_df = pd.real_csv('CadastroFuncionarios.csv', sep = ';', decimal = ';',)
print(funcionarios_df)
#arquivo excel
#funcionarios_df = pd.read_excel(CadastroFuncionarios.xls)
#Adicionar colunas
df['Nova Coluna']= df['Idade'] * 2
print(df)
#Removendo uma coluna
df.drop('Nova Coluna', axis=1, inplace=True)
print(df)
#Agrupamento por coluna e calculando  a idade média
grupo = df.groupby('Cidade')['Idade'].mean()
print(grupo)
#Ordenando dados de uma coluna
ordenados = df.sort_values(by='Idade')
print(ordenados)
"""
import pandas as pd

df = pd.read_excel('Produtos.xlsx', sheet_name='Planilha2', usecols=['Produtos', 'Preço Original'])
print(df)