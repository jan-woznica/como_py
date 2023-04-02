import streamlit as st
import pandas as pd 

st.header('Ahoj, vítej ve streamlitu')
st.markdown('Streamlit is **_really_ cool**.')
st.title('Dole je ještě něco víc cool')

if st.button('Click on button'):
    st.write('You are best')
else:
    st.write('nothing to see here')

st.header('Moje aplikace')
add_selectbox = st.sidebar.selectbox('Menu', ('Čtverec', 'Obdélník', 'Kvádr'))

if add_selectbox == ('Čtverec'):
    číslo = int(input('Vepište 1. číslo 1.'))
    obvod1 = (číslo * 4)
    obsah1 = (číslo*číslo)
    st.write(f'Obvod je {obvod1} a obsah je {obsah1}')
elif add_selectbox == ('Obdélník'):
    číslo1 = input('Vepište stranu a')
    číslo5 = input('Vepište stranu b')
    obvod2 = ((číslo1+číslo5)*2)
    obsah2 = číslo1*číslo5
    st.write(f'Obvod je {obvod2} a obsah je {obsah2}')
elif add_selectbox == ('Kvádr'):
    číslo2 = st.number_input('Vepište stranu a')
    číslo3 = st.number_input('Vepište stranu b')
    číslo4 = st.number_input('Vepište stranu c')
    objem = číslo2*číslo3*číslo4
    plocha = (2*(číslo2+číslo3)*(číslo3+číslo4)*(číslo2+číslo4))
    st.write(f'Objem je {objem} a plocha je {plocha}')


