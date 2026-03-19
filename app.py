import streamlit as st
import os

# Essential config
st.set_page_config(
    page_title="Control de Graduados - Ingeniería",
    page_icon="🎓",
    layout="wide"
)

from src.data.loader import load_data
from src.components.filters import apply_filters
from src.components.dashboard import render_dashboard
from src.components.table import render_table

def main():
    st.sidebar.title("🎓 UNILASALLISTA")
    st.sidebar.subheader("Facultad de Ingeniería")
    st.sidebar.markdown("---")
    
    menu = ["Dashboard Decanatura", "Vista Detallada"]
    choice = st.sidebar.radio("Menú Principal:", menu)
    st.sidebar.markdown("---")
    
    df = load_data()
    
    if df is not None:
        filtered_df = apply_filters(df)
        
        if choice == "Dashboard Decanatura":
            render_dashboard(filtered_df)
        elif choice == "Vista Detallada":
            render_table(filtered_df)
            
        st.sidebar.markdown("---")
        st.sidebar.caption("Aplicativo Analítico para la Decanatura de Ingeniería")

if __name__ == '__main__':
    main()
