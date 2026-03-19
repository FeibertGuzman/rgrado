import streamlit as st
import pandas as pd

def render_table(df: pd.DataFrame):
    st.title("🗂️ Vista Detallada de Registros")
    st.markdown("Tabla interactiva con los datos completos de los graduados. Utiliza la opción de descarga en la esquina superior derecha de la tabla para exportar a CSV.")
    
    st.write(f"Mostrando **{len(df)}** registros filtrados.")
    
    # Render dataframe
    st.dataframe(df, use_container_width=True, height=600)
    
    st.caption("Los datos presentados corresponden al cruce de filtros seleccionados en el panel izquierdo.")
