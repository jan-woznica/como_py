import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.success('Main page')
path = 'Wordertyp.csv'
path1 = 'Wordernázev.csv'
path2 = 'Worderamount.csv'
path3 = 'Worderpozice.csv'
path4 = 'Worderskupina.csv'
df_typ = pd.read_csv(path, sep = ';')
df_název = pd.read_csv(path1, sep = ';')
df_pozice = pd.read_csv(path3, sep = ';')
df_celek = pd.read_csv(path4, sep = ';' )
df_amount = pd.read_csv(path2, sep = ';')

df_c1 = df_celek.merge(df_název, how = "inner", on = ["Číslo"]).merge(df_pozice, how = "inner", on = ["Pozice"])

st.write(df_c1) 