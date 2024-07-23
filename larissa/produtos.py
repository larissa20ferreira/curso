import pandas as pd
import streamlit as st

st.title('Lendo Planiha de Produtos')
#filtrando por aba da planilha e colunas

df = pd.read_excel('Produtos.xlsz')

st.dataframe(df)