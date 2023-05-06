import streamlit as st
import pandas as pd
import numpy as np

st.title('Zóny')

url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_Sklad = pd.read_csv(path)
df_SkladZ = df_Sklad.loc[:,['Zóna', 'Regál', 'Pozice']]

hledání, Přidat1 = st.columns([8,1])
with hledání: df_SkladZ.loc[df_Sklad['Zóna'].str.contains(st.text_input('Vepište Název Zóny')),:]
with Přidat1: 
    st.write('')
    st.write('')
    přidat2 = st.button('Přidat', key='přidat4')

if přidat2:
    st.title('Zóny')
    with st.form('my_form'):
        with st.container():
            Zóna1 = st.text_input('Vepište název Zóny', key='Zóna2')
        with st.container():
            uložit1, storno2, uložit3 = st.columns([4,1,1])
            with uložit3: 
                submitted = st.form_submit_button("Uložit")
                if submitted:
                    df_SkladZ
df_SkladZ
