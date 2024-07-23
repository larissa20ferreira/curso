import streamlit as st
import pandas as pd 

pessoas = []

def cadastro(nome, fone):
    pessoa = {'nome':nome, 'Telefone': fone}
    pessoas.append(pessoa)
    st.title("Cadastrar Pessoa e Telefone")

with st.form(key='login_form'):
    nome = st.text_input('Nome da pessoa:')
    telefone = st.text_input('Telefone da pessoa:')
    botao = st.form_submit_button(label='Cadastrar')

if botao:
    if nome and telefone:
        cadastro(nome, telefone)
        st.success(f"{nome} com telefone {telefone} cadastrado com sucesso! ")
    else:
        st.error("Preencha todos os campos")

filtro = st.text_input("Buscar por nome: ")

if filtro:
    resultado = [pessoa for pessoa in pessoas if filtro.lower() in pessoa["Nome"].lower()]
else:
    resultados_filtrados = pessoas

if pessoas:
    st.write("### Pessoas Cadastradas")
    df = pd.DataFrame(pessoas)
    st.dataframe(df)
