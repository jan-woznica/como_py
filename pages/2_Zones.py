import streamlit as st
import pandas as pd
import numpy as np

st.title('Zóny')

#url = 'https://drive.google.com/file/d/1otRTVWp7W8mOAb1uEoFhfqdRUZz7sCUD/view?usp=share_link'
#path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
path = "Worder.csv"
path1 = "Worderzony.csv"
path2 = "Worderregaly.csv"
path3 = "Worderpozice.csv"
#df_Sklad = pd.read_csv(path)
#df_SkladZ = df_Sklad.loc[:,['Zóna', 'Regál', 'Pozice']]
df_zony = pd.read_csv(path1, sep = ';')
df_regaly = pd.read_csv(path2, sep = ';')
df_pozice = pd.read_csv(path3, sep = ';')

tab1, tab2, tab3 = st.tabs(['Zóna', 'Regál', 'Pozice'])
with tab1:
    st.title('Pozice')
    with st.container():
        sloup1, sloup2, sloup3 = st.columns([1,1,1])
        with sloup1:
            r1 = st.selectbox('Vyberte zónu ve které je pozice', options = df_regaly['Zóna'].unique())
        with sloup2:
            if r1 is None:
                r2 = st.selectbox('Vyberte regál ve které je pozice', options = df_regaly['Regál'] )
            else:
                r2 = st.selectbox('Vyberte regál ve které je pozice', options = df_regaly[df_regaly["Zóna"] == r1]['Regál'] )
        with sloup3:
            pozice1 = st.text_input('Vepište název pozice', key='pozice2', max_chars=5)
    btn_add_pozice = st.button('Přidat_pozici')
    if btn_add_pozice:
        df_add_pozice = pd.DataFrame(zip([r1], [r2], [pozice1]))
        st.write(df_add_pozice)
        df_add_pozice.columns = ['Zóna', 'Regál', 'Pozice']
        df_pozice = pd.concat([df_pozice, df_add_pozice], axis = 0)
        df_pozice.to_csv(path3, sep = ";", index = False)
        st.experimental_rerun()
with tab2:
    st.title('Regály')
    with st.container():
        sl1, sl2 = st.columns([1,1])
        with sl1:
            z1 = st.selectbox("Vyberte zonu ve které je regál", options = df_zony["Zóna"])
        with sl2:
            Regál1 = st.text_input('Vepište název Regálu', key='Regál2', max_chars=5)
    btn_add_regaly = st.button('Přidat_Regál')
    if btn_add_regaly:
        df_add_regaly = pd.DataFrame(zip([Regál1], [z1]))
        st.write(df_add_regaly)
        df_add_regaly.columns = ['Regál', 'Zóna']
        df_regaly = pd.concat([df_regaly, df_add_regaly], axis = 0)
        df_regaly.to_csv(path2, sep = ";", index = False)
        st.experimental_rerun()
with tab3:
    st.title('Zóny')
    with st.container():
        Zóna1 = st.text_input('Vepište název Zóny', key='Zóna2', max_chars=5)
    with st.container():
        uložit1, storno2, uložit3 = st.columns([4,1,1])
        with uložit3: 
            btn_add_zona = st.button("Uložit")
    if btn_add_zona:
        df_add = pd.DataFrame([Zóna1])
        df_add.columns = ["Zóna"]
        df_zony = pd.concat([df_zony, df_add], axis = 0)
        df_zony.to_csv(path1, sep = ";", index = False)
        st.experimental_rerun()
