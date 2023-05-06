import streamlit as st
import pandas as pd
import numpy as np

url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_Sklad = pd.read_csv(path)
df_SkladZ = df_Sklad.loc[:,['Zóna', 'Regál', 'Pozice']]

wt = ['initialised text']
ss = df_SkladZ(wt=wt)

st.header('Watchlist')

container1 = st.beta_container()
sym = container1.text_input('for adding')
container2 = st.beta_container()
add_button = container2.button('add')

if add_button:
    ss.wt.append(sym)

st.write(ss.wt)

