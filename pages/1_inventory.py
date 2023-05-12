import streamlit as st
import pandas as pd
import numpy as np

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

tab1, tab2, tab3, tab4 = st.tabs(['Sklad', 'Množství', 'Produkt', 'Typ'])
with tab1: 
    df_c1 = df_celek.merge(df_název, how = "inner", on = ["Název"]).merge(df_pozice, how = "inner", on = ["Pozice"])
    df_c1 = st.experimental_data_editor(df_c1, num_rows="dynamic")
with tab2:
    st.title('Množství')
    slp,slp2,slp3 = st.columns([1,2,2])
    with slp:
        množství = st.number_input('Vepište množsství', min_value = -10, max_value = 100, value = 0, key='číslo3')
    with slp2:
        č1 = st.selectbox('Vyberte název produktu', options = df_název['Název'])
    with slp3:
        p1 = st.selectbox('Vyberte pozici produktu', options = df_pozice['Pozice'])
    btn_add_celek = st.button('Propojit')
    if btn_add_celek:
        df_add_celek = pd.DataFrame(zip([množství], [č1], [p1]))
        st.write(df_add_celek)
        df_add_celek.columns = ['Množství', 'Název', 'Pozice']
        df_celek = pd.concat([df_celek, df_add_celek], axis = 0)
        df_celek = df_celek.groupby(["Název", "Pozice"]).sum().reset_index()
        df_celek.to_csv(path4, sep = ";", index = False)
        st.experimental_rerun()
    df_celek.loc[df_celek['Název'].str.contains(st.text_input('Vepište název pro vyhledání množství')),:]
with tab3:
    st.title('Název')
    with st.container():
        sl1, sl2, sl3 = st.columns([1,1,1])
        with sl1:
            t1 = st.selectbox('Vyberte Typ produktu', options = df_typ['Typ'])
        with sl2:
            Název1 = st.text_input('Vepište Název produktu', key='Název2', max_chars=10)
        with sl3:
            číslo = st.number_input('Vepište číslo produktu', value = max(df_název["Číslo"], default = 0) + 1 , key='číslo2', disabled = True)
        btn_add_produkt = st.button('Přidat_produkt')
        if btn_add_produkt:
            df_add_produkt = pd.DataFrame(zip([Název1], [t1], [číslo]))
            st.write(df_add_produkt)
            df_add_produkt.columns = ['Název', 'Typ', 'Číslo']
            df_název = pd.concat([df_název, df_add_produkt], axis = 0)
            df_název.to_csv(path1, sep = ";", index = False)
            st.experimental_rerun()
        df_název.loc[df_název['Název'].str.contains(st.text_input('Vepište název pro vyhledání')),:]
with tab4:
    st.title('Typ')
    with st.container():
        Typ1 = st.text_input('Vepište Typ pro přidání', key='Typ2', max_chars=10)
        with st.container():
            uložit1, storno2, uložit3 = st.columns([4,1,1])
            with uložit3: 
                btn_add_typ = st.button("Uložit")
        if btn_add_typ:
            df_add_typ = pd.DataFrame([Typ1])
            df_add_typ.columns = ['Typ']
            df_typ = pd.concat([df_typ, df_add_typ], axis = 0)
            df_typ.to_csv(path, sep = ";", index = False)
            st.experimental_rerun()
        df_typ.loc[df_typ['Typ'].str.contains(st.text_input('Vepište typ pro vyhledání')),:]