import streamlit as st
import pandas as pd

def apply_filters(df: pd.DataFrame) -> pd.DataFrame:
    st.sidebar.markdown("### 🔍 Filtros de Búsqueda")
    
    filtered_df = df.copy()
    
    # Generic wide search on all text-like columns
    search = st.sidebar.text_input("Buscar texto libre (Ej. Nombre o Doc):", "")
    if search:
        mask = filtered_df.astype(str).apply(lambda x: x.str.contains(search, case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]
        
    # Program filter (attempting to auto-detect the program column)
    program_col = next((col for col in filtered_df.columns if 'programa' in col.lower() or 'carrera' in col.lower()), None)
    
    if program_col:
        programs = ["Todos"] + sorted([str(p) for p in filtered_df[program_col].dropna().unique()])
        selected_program = st.sidebar.selectbox("Filtrar por Programa:", programs)
        if selected_program != "Todos":
            filtered_df = filtered_df[filtered_df[program_col].astype(str) == selected_program]
            
    # Period filter (if a period column exists)
    period_col = next((col for col in filtered_df.columns if 'periodo' in col.lower() or 'semestre' in col.lower()), None)
    if period_col:
        periods = ["Todos"] + sorted([str(p) for p in filtered_df[period_col].dropna().unique()])
        selected_period = st.sidebar.selectbox("Filtrar por Periodo:", periods)
        if selected_period != "Todos":
            filtered_df = filtered_df[filtered_df[period_col].astype(str) == selected_period]

    return filtered_df
