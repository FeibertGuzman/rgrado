# Control de Graduados - Facultad de Ingeniería 🎓

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Aplicación web básica construida con Streamlit para llevar el control de los estudiantes que se han graduado en la facultad de ingeniería (4 programas) en UNILASALLISTA.

## Requisitos Previos

- Python 3.9 o superior
- Un archivo Excel llamado `Requisito de Grado UNILASALLISTA.xlsx` en la raíz del proyecto.

## Instalación y Ejecución Local

1. Clonar el repositorio.
2. Crear un entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar el entorno virtual:
   - **Windows:** `venv\Scripts\activate`
   - **macOS/Linux:** `source venv/bin/activate`
4. Instalar las dependencias locales:
   ```bash
   pip install -r requirements.txt
   ```
5. Asegurarse de tener el archivo Excel `Requisito de Grado UNILASALLISTA.xlsx` en la misma carpeta.
6. Ejecutar la aplicación:
   ```bash
   streamlit run app.py
   ```

## Despliegue en Streamlit Community Cloud

Esta aplicación está lista para ser desplegada en Streamlit Community Cloud articulada con GitHub:
1. Sube este código a un repositorio público (o privado) en GitHub.
2. Entra a [share.streamlit.io](https://share.streamlit.io/).
3. Conecta tu cuenta de GitHub.
4. Selecciona el repositorio, la rama principal y el archivo `app.py`.
5. ¡Haz clic en **Deploy**!
