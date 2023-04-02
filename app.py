import streamlit as st
import pandas as pd 

st.header('Ahoj, vítej ve streamlitu')
st.markdown('Streamlit is **_really_ cool**.')
st.title('Dole je ještě něco víc cool')

if st.button('Click on button'):
    st.write('You are best')
else:
    st.write('nothing to see here')


hodnota = input('Vepište jméno a příjmení')
hodnota1 = input('datum narpzení')

values = st.slider(
    'Select a range of values',
    0., 2020.0, (250, 2000))
st.write('Values:', values)



