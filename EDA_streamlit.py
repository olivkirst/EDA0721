import pandas as pd
import streamlit as st
import csv
import seaborn as sns
import matplotlib.pyplot as plt


dfc_all= pd.read_csv(r".\Output_data\all_coord_only_all_wells.csv", sep=",")
dfc_dts= pd.read_csv(r".\Output_data\\all_coord_only_well_dts.csv", sep=",")
dfc_final= pd.read_csv(r".\Output_data\\all_coord_only_well_dts_final.csv", sep=",")
df= pd.read_csv(r".\Output_data\\well_dts_final.csv", sep=",")
st.set_page_config(layout="wide")

# returns ','
# Sidebar config
add_file = st.sidebar.file_uploader('Otros datos oara cargar si necesario', type = 'csv')
if add_file is not None: #
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(add_file)
    separator = dialect.delimiter
    df = pd.read_csv(add_file, sep = separator)
page = st.sidebar.selectbox(
    'Menu',
    ('home', 'datos', 'filtrado')
)

# Main page
def main_page():
    st.title('ANALISIS DE DATOS DE POZOS DE OIL & GAS')
    st.markdown('<h2>Analisis elástica', unsafe_allow_html = True)
    with st.beta_expander('Origen de los datos'):
        st.write('The well log data used in this repo is licensed as Norwegian License for Open Government Data (NLOD) 2.0. '
                 '“Lithofacies data was provided by the FORCE Machine Learning competition with well logs and seismic 2020”. ')
# st.balloons()
    with st.echo():
        st.write("Esta forma tienen nuestros datos")
        st.dataframe(df)

def datos():

    st.title('Localizacíon de los pozos')
    st.markdown('## Mapa con todos los pozos (98)')
    st.map(data =dfc_all)
    st.markdown('## Mapa con todos los pozos con DTS (32)')
    st.map(data = dfc_dts)
    st.markdown('## Mapa con los pozos para análisis cuantitativa (5) ')
    st.map(data = dfc_final)

if page == 'home':
    main_page()
elif page == 'datos':
    datos()