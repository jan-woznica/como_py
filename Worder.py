import streamlit as st
import pandas as pd
import numpy as np

st.write('Menu')
st.write('tohle je pakárna')

st.sidebar.success('Main page')

url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_Sklad = pd.read_csv(path)
st.write(df_Sklad)

st.container()
with st.container():
    přidat1, přidat2 = st.columns([8,1])
    with přidat2:
        přidat = st.button('Přidat', key='přidat3')

st.write('tohle je mimo')

if přidat == True:
    st.container()
    with st.container():
        sloupec1, sloupec2 = st.columns([8,1])
        with sloupec1:
            with st.container():
                názv1, type2 = st.columns(2)
                with názv1: Název = st.text_input('Název produktu', key='Název1')
                with type2: Typ = st.selectbox('Vyberte typ produktu',('Světla', 'Nářadí', 'Další'), key='Typ1')
            with st.container():
                symb1, čísl2 = st.columns(2)
                with symb1: Symbol = st.text_input('Symbol produktu', key='Symbol1')
                with čísl2: Číslo = st.number_input('Vepište číslo produktu',0, key='Číslo1')
            with st.container():
                col1, col2, col3 = st.columns(3)
                with col1: Zóna = st.selectbox('Vyberte zónu',('Patro', 'Sklep'), key='Zóna1')
                with col2: Regál = st.selectbox('Vyberte regál',('One', 'Two'), key='Regál1')
                with col3: Pozice = st.selectbox('Vyberte pozici',('1B', '1C'), key='Pozice1')
        with sloupec2: foto = st.button('Přidat foto')
    with st.container():
        uložit1, storno2, uložit3 = st.columns([6,1,1])
        with storno2: storno = st.button('Storno', key='storno1')
        with uložit3: uložit = st.button('Uložit', key='uložit4')
        if st.session_state.storno1 == True: 
            st.session_state.přidat3 = False
        if st.session_state.uložit4 == True: 
            st.session_state.přidat3 = False

st.session_state.přidat3
st.session_state.Název1
st.session_state.Typ1
st.session_state.Symbol1
st.session_state.Číslo1
st.session_state.Zóna1
st.session_state.Pozice1
st.session_state.Regál1
st.session_state.storno1

if 'přidat1' not in st.session_state:
    st.session_state.přidat3 = False
elif 'přidat' in st.session_state:
    st.session_state.přidat3 = True
