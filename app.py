import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title="Control de Graduados - Facultad de Ingeniería",
    page_icon="🎓",
    layout="wide"
)

st.title("🎓 Control de Estudiantes Graduados")
st.subheader("Facultad de Ingeniería - Corporación Universitaria Lasallista (UNILASALLISTA)")

st.markdown("""
Esta aplicación permite visualizar el estado y los requisitos de grado de los estudiantes de la Facultad de Ingeniería en sus 4 programas.
""")

EXCEL_FILE = "Requisito de Grado UNILASALLISTA.xlsx"

@st.cache_data
def load_data():
    if os.path.exists(EXCEL_FILE):
        try:
            df = pd.read_excel(EXCEL_FILE)
            return df
        except Exception as e:
            st.error(f"Error al leer el archivo Excel: {e}")
            return None
    else:
        return None

df = load_data()

if df is not None:
    st.success(f"✅ Archivo Excel '{EXCEL_FILE}' cargado correctamente.")
    
    st.markdown("### Datos de los Estudiantes")
    
    # Generic text search
    search = st.text_input("🔍 Buscar estudiante (por nombre, documento o programa si aplica):", "")
    
    if search:
        # Filter all string columns for the search term
        mask = df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)
        st.dataframe(df[mask], use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)
        
    st.markdown("### Resumen")
    st.write(f"Total de registros: **{len(df)}**")
else:
    st.warning(f"⚠️ No se encontró el archivo Excel: `{EXCEL_FILE}`. Por favor, asegúrese de cargarlo en la misma carpeta.")

st.markdown("---")
st.caption("Desarrollado para la Facultad de Ingeniería")
