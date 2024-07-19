#pip instalit pandas

#Renomeia a biblioteca desejada
"""import streamlit as st 

st.title(" Título da página ")
st.header('Cabeçalho')
st.subheader('Sub cabeçalho')
st.text('Texto simples')

st.markdown('Título Markdown')

valor = st.slider('Selecione um valor', 0, 100, 50)
st.write('Valor selecionado:', valor)

if st.button('Clique aqui '):
    st.write('Botão clicado')

nome = st.text_input('Digite seu nome: ')
st.write("Nome:",nome)

opcao = st.selectbox('Escolha uma opção:', ['op 1', 'op 2', 'op 3'])
st.write('Opção escolhida:', opcao)

opcoes = st.multiselect('Escolha multiplas opções: ', ['op 1', 'op 2', 'op 3'])
st.write('Opções escolhidas:', opcoes) 

arquivo = st.file_uploader('Escolha um arquivo ')
if arquivo is not None:
    st.write('Arquivo carregado:', arquivo.name)

if st.checkbox('Mostrar texto'):
    st.write('Texto mostrado!')

genero = st.radio('Escolha seu gênero: ', ['Masculino', 'Feminino', 'Outro'])
st.write('Gênero:', genero)

import matplotlib.pyplot as pit

fig, ax = pit.subplots()
ax.plot([1,2,3,4,5], [10,20,30,40,50])
st.pyplot(fig)

col1 , col2 = st.columns(2)
col1.write('Coluna 1')
col2.write('Coluna 2')
#Barras lateral
st.sidebar.title('Barra Lateral')
st.sidebar.slider('Slide na barra lateral', 0,100,50)
#Expensor
with st.expander('Clique aqui para exoandir'):
    st.write('Texto dentro do expansor')

tab1, tab2 = st.tabs(['Tab1', 'Tab2'])
with tab1:
    st.write('Contendo a tab 1')
    st.line_chart([1,2,3,4])
with tab2:
    st.write('Contendo a tab 2')
    st.bar_chart([5,10,15,20])

st.image('gremio2.png',width=225)"""





"""import streamlit as st

def login(usuario,senha):
    loginCerto = "larissa"
    senhaCerta = "07072007"
    return usuario == loginCerto and senha == senhaCerta
st.title('Tela de login')

with st.form(key='login_form'):
        usuario = st.text_input('Nome de usuário: ')
        senha = st.text_input('Digite senha: ')
        botao = st.form_submit_button(label='Entrar')

if botao:
    if login(usuario, senha):
          st.success('Login bem sucedido!')
          st.write('Bem vindo')
    else:
         st.error('Nome de usuário e senha incorretos.')
"""

import streamlit as st
def cadastro(nome, fone):
    pessoa = {'nome':nome, 'telefone': fone}
    

    pessoa.append(pessoa)

with st.form(key='login_form'):
    nome = st.text_input('Nome da pessoa:')
    telefone = st.text_input('Telefone da pessoa:')
    botao = st.form_submit_button(label='Cadastrar')

if botao:
    if nome and telefone:
        cadastro(nome, telefone)
        st.success()


