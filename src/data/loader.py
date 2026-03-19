import streamlit as st
import pandas as pd
import os

EXCEL_FILE = "Requisito de Grado UNILASALLISTA.xlsx"

@st.cache_data
def load_data():
    if os.path.exists(EXCEL_FILE):
        try:
            df = pd.read_excel(EXCEL_FILE)
            # Here we could implement more advanced logic: dropping NA, standardizing columns, etc.
            return df
        except Exception as e:
            st.error(f"Error al leer el archivo Excel: {e}")
            return None
    else:
        st.warning(f"⚠️ No se encontró el archivo Excel: `{EXCEL_FILE}`. Asegúrese de que existe en la carpeta principal.")
        return None
