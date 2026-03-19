import streamlit as st
import pandas as pd
import plotly.express as px

def render_dashboard(df: pd.DataFrame):
    st.title("📊 Dashboard Decanatura")
    st.markdown("Indicadores clave de rendimiento y distribución de graduados de la Facultad de Ingeniería.")
    
    if df.empty:
        st.warning("No hay registros que coincidan con los filtros seleccionados.")
        return
        
    # Top Level KPIs
    st.markdown("### Indicadores Principales")
    kpi1, kpi2, kpi3 = st.columns(3)
    
    total_registros = len(df)
    kpi1.metric(label="Total Registros Listados", value=f"{total_registros:,}")
    
    # Attempt to find useful columns for stats
    program_col = next((col for col in df.columns if 'programa' in col.lower() or 'carrera' in col.lower()), None)
    estado_col = next((col for col in df.columns if 'estado' in col.lower() or 'status' in col.lower()), None)
    
    if program_col:
        kpi2.metric(label="Programas Activos", value=df[program_col].nunique())
    else:
        kpi2.metric(label="Columnas Cargadas", value=len(df.columns))
        
    if estado_col:
        kpi3.metric(label="Estados Diferentes", value=df[estado_col].nunique())
        
    st.markdown("---")
    
    # Graphs Section
    st.markdown("### Análisis Gráfico")
    col1, col2 = st.columns(2)
    
    if program_col:
        with col1:
            prog_counts = df[program_col].value_counts().reset_index()
            prog_counts.columns = [program_col, 'Cantidad']
            
            fig_bar = px.bar(
                prog_counts, 
                x=program_col, 
                y='Cantidad', 
                title="Cantidad de Registros por Programa",
                color=program_col,
                text_auto=True
            )
            fig_bar.update_layout(xaxis_title="Programa", yaxis_title="Graduados")
            st.plotly_chart(fig_bar, use_container_width=True)
            
        with col2:
            fig_pie = px.pie(
                prog_counts, 
                values='Cantidad', 
                names=program_col, 
                title="Proporción por Programa",
                hole=0.4
            )
            st.plotly_chart(fig_pie, use_container_width=True)
    else:
        st.info("💡 Consejo: Asegúrate de que tu Excel contenga una columna llamada 'Programa' para activar las gráficas por segmento.")
