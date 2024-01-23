from pathlib import Path
import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title
import pandas as pd

st.set_page_config(
    layout="wide"
)

lista = [1,2,3]

show_pages([
    Page('1_Menu_Principal.py','Menu Principal'),
    Page('pages/2_Planejamento.py','CPT')
])

pasta_datasets = Path(__file__).parent/'datasets'
caminho_CPT = pasta_datasets/'CPT - MATRIZ.csv'
df_CPT = pd.read_csv(caminho_CPT,decimal=',',sep=';')

st.dataframe(df_CPT)

teste1 = st.date_input("Escolha uma data:")
st.write(teste1.year)

