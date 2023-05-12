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

tab1, tab2, tab3 = st.tabs(['Množství', 'Produkt', 'Typ'])
with tab1:
    a1, a2 = st.columns([6,1])
    with a2:
        btn_for_form_sklad = st.button('Přidat')
    if btn_for_form_sklad:
        with st.form('Formulář'):
            slp,slp2,slp3 = st.columns([2,2,2])
            with slp:
                množství = st.number_input('Vepište množsství', min_value = -10, max_value = 100, value = 0, key='číslo3')
            with slp2:
                č1 = st.selectbox('Vyberte název produktu', options = df_název['Název'])
            with slp3:
                p1 = st.selectbox('Vyberte pozici produktu', options = df_pozice['Pozice'])
            slp4, slp5 = st.columns([6,1])
            with slp5:
                submitted_sklad = st.form_submit_button("Přidat množství")
            if submitted_sklad:
                df_add_celek = pd.DataFrame(zip([množství], [č1], [p1]))
                st.write(df_add_celek)
                df_add_celek.columns = ['Množství', 'Název', 'Pozice']
                df_celek = pd.concat([df_celek, df_add_celek], axis = 0)
                df_celek = df_celek.groupby(["Číslo", "Pozice"]).sum().reset_index()
                df_celek.to_csv(path4, sep = ";", index = False)
                st.experimental_rerun()
with tab2:
    st.title('Produkt')
    ad1, ad2 = st.columns([6,1])
    with ad2:
        btn_for_form_produkt = st.button('Přidat produkt')
    if btn_for_form_produkt:
        with st.form('Formulář'):
            sl1, sl2, sl3 = st.columns([1,1,1])
            with sl1:
                t1 = st.selectbox('Vyberte Typ produktu', options = df_typ['Typ'])
            with sl2:
                Název1 = st.text_input('Vepište Název produktu', key='Název2', max_chars=10)
            with sl3:
                číslo = st.number_input('Vepište číslo produktu', value = max(df_název["Číslo"], default = 0) + 1 , key='číslo2', disabled = True)
            sl4, sl5 = st.columns([6,1])
            with sl5:
                submitted_produkt = st.form_submit_button("Přidat produkt")
            if submitted_produkt:
                df_add_produkt = pd.DataFrame(zip([Název1], [t1], [číslo]))
                st.write(df_add_produkt)
                df_add_produkt.columns = ['Název', 'Typ', 'Číslo']
                df_název = pd.concat([df_název, df_add_produkt], axis = 0)
                df_název.to_csv(path1, sep = ";", index = False)
                st.experimental_rerun()
with tab3:
    st.title('Typ')
    add1, add2 = st.columns([6,1])
    with add2:
        btn_for_form_typ = st.button('Přidat typ')
    if btn_for_form_typ:
        with st.form('Formulář_typ'):
            Typ1 = st.text_input('Vepište Typ', key='Typ2', max_chars=10)
            s4, s5 = st.columns([6,1])
            with s5:
                submitted_typ = st.form_submit_button("Přidat typ")
            if submitted_typ:
                df_add_typ = pd.DataFrame([Typ1])
                df_add_typ.columns = ['Typ']
                df_typ = pd.concat([df_typ, df_add_typ], axis = 0)
                df_typ.to_csv(path, sep = ";", index = False)
                st.experimental_rerun()
        st.write(df_typ)

'''
hledání, Přidat1 = st.columns([8,1])
with hledání: 
    df_SkladZ.loc[df_Sklad['Zóna'].str.contains(st.text_input('Vepište Název Zóny')),:]
    st.text("Přidat pro přidání")
'''
'''
url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_Sklad = pd.read_csv(path)
df_SkladZ = df_Sklad.loc[:,['Zóna', 'Regál', 'Pozice']]

url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df_Sklad = pd.read_csv(path)
st.write(df_Sklad)
'''
        #pro multi filtr (multiselect)
 #           options = st.multiselect(
#   'What are your favorite colors',
  #  ['Green', 'Yellow', 'Red', 'Blue'],
 #   ['Yellow', 'Red'])
#st.write('You selected:', options)

#multiselect
#vyzkoušet st.camera_input
#vxkoušet st.error a další
#zvážiz st.forms
#kouknout na st.help
#sessions state
#st.cache
#nahrávání ze souboru