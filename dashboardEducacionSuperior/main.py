# --- LIBRERÍAS ----

import streamlit as st                         # Importa Streamlit, la librería en la cual se basa todo el dashboard
from streamlit_option_menu import option_menu  # Decora los menús (barras con filtros)
import pandas as pd                            # Pandas pu, como no cachai pandas
import plotly.express as px                    # Para hacer los gráficos
from pathlib import Path
# --- CONFIGURACIONES GENERALES DE LA APP ----

st.set_page_config(page_title="Dashboard Educación Superior",
                   layout="wide",
                   initial_sidebar_state="expanded")



logo_path = Path(__file__).parent / "imagenes" / "logoCriteria.png"
st.logo(str(logo_path), size="large")

# --- Cargar el CSS donde se configura los detalles estéticos ---
try:
    with open("estilo.css") as f: 
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("Error: Archivo 'estilo.css' no encontrado. Asegúrate de que esté en la misma carpeta.")



# --- Barra horizontal ----

barra_vertical = option_menu(
    menu_title="",
    options=["Matriculados", "Titulados", "Fuga"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#f9f9f9"},
        "nav-link": {
            "font-size": "16px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#E6E6FA"  # lavanda claro al pasar el mouse
        },
        "nav-link-selected": {
            "background-color": "#73277F",  # morado oscuro 
            "color": "white"
        }
    }
)
BASE = Path(__file__).parent  # carpeta donde está main.py
csv_titulados = BASE / "datos" / "titulados.csv"
csv_matriculas = BASE / "datos" / "matriculas.csv"  # si tienes más
df_titulados = pd.read_csv(csv_titulados)
df_matriculas = pd.read_csv(csv_matriculas)
df_seleccionado = df_matriculas.copy()


# Selección del DataFrame según la opción clickeada
if barra_vertical == "Titulados":
    df_seleccionado = df_titulados.copy()
elif barra_vertical == "Matriculados":
    df_seleccionado = df_matriculas.copy()
# --- Barra Lateral con el Menú Principal y los Filtros Desplegables ---
with st.sidebar:
    # AÑO
    años_disponibles = sorted(df_seleccionado["año"].unique())
    años_disponibles = ["Todos"] + list(años_disponibles)
    año_seleccionado = st.selectbox("Año", años_disponibles)

    if año_seleccionado != "Todos":
        df_filtrado = df_seleccionado[df_seleccionado["año"] == año_seleccionado]
    else:
        df_filtrado = df_seleccionado.copy()

    # TIPO DE INSTITUCION
    tipos_disponibles = sorted(df_filtrado["tipo institucion"].unique())
    tipos_disponibles = ["Todos"] + list(tipos_disponibles)
    tipo_seleccionado = st.selectbox("Tipo de institución", tipos_disponibles)

    if tipo_seleccionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado["tipo institucion"] == tipo_seleccionado]

    # INSTITUCION
    instituciones_disponibles = sorted(df_filtrado["institucion"].unique())
    instituciones_disponibles = ["Todos"] + list(instituciones_disponibles)
    institucion_seleccionada = st.selectbox("Institución:", instituciones_disponibles)

    if institucion_seleccionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["institucion"] == institucion_seleccionada]

    # AREA
    areas_disponibles = sorted(df_filtrado["area"].unique())
    areas_disponibles = ["Todos"] + list(areas_disponibles)
    area_seleccionada = st.selectbox("Área:", areas_disponibles)

    if area_seleccionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["area"] == area_seleccionada]

    # CARRERA
    carreras_disponibles = sorted(df_filtrado["carrera"].unique())
    carreras_disponibles = ["Todos"] + list(carreras_disponibles)
    carrera_seleccionada = st.selectbox("Carrera:", carreras_disponibles)

    if carrera_seleccionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["carrera"] == carrera_seleccionada]

    # MODALIDAD
    modalidades_disponibles = sorted(df_filtrado["modalidad"].unique())
    modalidades_disponibles = ["Todos"] + list(modalidades_disponibles)
    modalidad_seleccionada = st.selectbox("Modalidad:", modalidades_disponibles)

    if modalidad_seleccionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["modalidad"] == modalidad_seleccionada]

    # JORNADA
    jornadas_disponibles = sorted(df_filtrado["jornada"].unique())
    jornadas_disponibles = ["Todos"] + list(jornadas_disponibles)
    jornada_seleccionada = st.selectbox("Jornada:", jornadas_disponibles)

    if jornada_seleccionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado["jornada"] == jornada_seleccionada]
        


# with st.sidebar:

#     # AÑO
#     años_disponibles = df_seleccionado.año.unique()
#     año_seleccionado = st.selectbox("Año", años_disponibles)

#     #TIPO DE institucion
#     tipos_disponibles = df_seleccionado['tipo institucion'].unique()
#     tipo_seleccionado = st.selectbox("Tipo de institucion", tipos_disponibles)

#     # institucion
#     instituciones_disponibles = df_seleccionado.institucion.unique()
#     institucion_seleccionada = st.selectbox("institucion:", instituciones_disponibles)

#     # AREA
#     areas_disponibles = df_seleccionado.area.unique()
#     area_seleccionada = st.selectbox("Área:", areas_disponibles)

#     # CARRERA 
#     carreras_disponibles = df_seleccionado.carrera.unique()
#     carrera_seleccionada = st.selectbox("Carrera:", carreras_disponibles)

#     # modalidad
#     modalidades_disponibles = df_seleccionado.modalidad.unique()
#     modalidad_seleccionada = st.selectbox("modalidad:", modalidades_disponibles)

#     # jornada
#     jornadas_disponibles = df_seleccionado.jornada.unique()
#     jornada_seleccionada = st.selectbox("jornada:", jornadas_disponibles)

    # st.markdown("---")
    # st.caption("Nota: Los datos utilizados son solo de ejemplo.")

# --- Datos de ejemplo ---

# data_modalidad = {
#     'modalidad': ['Presencial', 'Online', 'Híbrida', 'Presencial', 'Online', 'Híbrida'],
#     'cantidad': [25000, 3000, 1000, 12000, 4000, 10000]
# } 
data_modalidad = df_filtrado[['modalidad', 'cantidad']]
data_jornada = df_filtrado[['jornada', 'cantidad']]

df_modalidad = pd.DataFrame(data_modalidad)
df_jornada = pd.DataFrame(data_jornada)
# Agrupar los datos por 'jornada' y sumar las matrículas para el gráfico de torta
df_agrupado_jornada = df_jornada.groupby('jornada')['cantidad'].sum().reset_index()

# Agrupar los datos por 'modalidad' y sumar las matrículas para el gráfico de torta
df_agrupado_modalidad = df_modalidad.groupby('modalidad')['cantidad'].sum().reset_index()

# --- Contenido del dashboard ---

st.caption(f"Filtros activos: {institucion_seleccionada} {año_seleccionado}")

col1, col2 = st.columns([.7, 2])

with col1:
    st.metric("Número de matrículas", df_filtrado['cantidad'].sum())

    # --- Gráfico de Torta con Plotly Express (modalidad) ---
    fig_modalidad = px.pie(
        df_agrupado_modalidad,
        values='cantidad',
        names='modalidad',
        title='Modalidad',
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Purples_r,
        height=220 
    )

    # Opcional: Personalizar el layout del gráfico
    fig_modalidad.update_traces(textposition='inside', textinfo='percent+label')
    fig_modalidad.update_layout(
        showlegend=True,
        margin={"l":0, "r":0, "t":30, "b":0} # Ajusta los márgenes internos del gráfico
    )

    # --- Mostrar el Gráfico en Streamlit ---
    st.plotly_chart(fig_modalidad, use_container_width=True)


    # --- Gráfico de Torta (jornada) ---
    fig_jornada = px.pie(
        df_agrupado_jornada,
        values='cantidad',
        names='jornada',
        title='Jornada',
        hole=0.3,
        color_discrete_sequence=px.colors.sequential.Purples_r,
        height=220 
    )

    # Personalizar el layout del gráfico
    fig_jornada.update_traces(textposition='inside', textinfo='percent+label')
    fig_jornada.update_layout(
        showlegend=True,
        margin={"l":0, "r":0, "t":30, "b":0}
    )

    # --- Mostrar el Gráfico en Streamlit ---
    st.plotly_chart(fig_jornada, use_container_width=True)

with col2:
    # Creo dos sub-columnas
    col_a, col_b = st.columns(2)
    with col_a:
        st.subheader("Distribución de Instituciones")

        # Agrupar por institución y sumar la cantidad
        df_instituciones = df_filtrado.groupby('institucion', as_index=False)['cantidad'].sum()

        # Calcular el total de matrículas
        total_matriculas = df_instituciones['cantidad'].sum()

        # Calcular el % del total
        df_instituciones['% del total'] = (df_instituciones['cantidad'] / total_matriculas * 100).round(2)

        # --- Mostrar solo instituciones ---
        st.dataframe(df_instituciones, hide_index=True, height=210)


    with col_b:
        st.subheader("Distribución de Carreras")

        # Excluir "Total" en caso de que venga de df_filtrado
        df_filtrado_sin_total = df_filtrado[~df_filtrado['carrera'].str.strip().str.lower().eq('total')]

        # Agrupar por carrera y sumar la cantidad
        df_instituciones = df_filtrado_sin_total.groupby('carrera', as_index=False)['cantidad'].sum()

        # Calcular el total de matrículas
        total_matriculas = df_instituciones['cantidad'].sum()

        # Calcular el % del total
        df_instituciones['% del total'] = (df_instituciones['cantidad'] / total_matriculas * 100).round(2)

        # --- Mostrar solo carreras ---
        st.dataframe(df_instituciones, hide_index=True, height=210)

    

    # --- Ejemplo para el Gráfico Evolutivo ---

    # data_evolutivo = {
    #     'Año': list(range(2015, 2025)),
    #     'cantidad': [4.5, 2.8, 4.0, 5.5, 7.0, 4.0, 8.5, 9.5, 11.5, 12.5]
    # }
    # df_evolutivo = pd.DataFrame(data_evolutivo)
    df_evolutivo = df_filtrado.groupby('año')['cantidad'].sum().reset_index()
    

    # --- Gráfico de Línea con Plotly Express ---
    fig_evolutivo = px.line(
        df_evolutivo,
        x='año',
        y='cantidad',
        title='Evolutivo cantidad',
        markers=True, # Muestra puntos en cada dato
        height=300, # Altura del gráfico en píxeles
        color_discrete_sequence=['#9400D3'] # color morado 
    )


    # --- Mostrar el Gráfico en Streamlit ---

    st.plotly_chart(fig_evolutivo, use_container_width=True)


