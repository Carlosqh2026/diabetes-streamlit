import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Análisis de diabetes",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Sistema de análisis de diabetes")
st.write("Explora los datos de los pacientes.")

df = pd.read_csv("dataset_diabetes_limpio.csv")

st.subheader("Vista general de los datos")
st.dataframe(df, use_container_width=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total de pacientes", len(df))

with col2:
    st.metric("Casos con diabetes", int((df["diabetes"] == 1).sum()))

with col3:
    st.metric("Casos sin diabetes", int((df["diabetes"] == 0).sum()))

st.subheader("Filtrar pacientes")

edad_max = int(df["edad"].max())
edad_min = int(df["edad"].min())

edades = st.slider(
    "Selecciona el rango de edad",
    min_value=edad_min,
    max_value=edad_max,
    value=(edad_min, edad_max)
)

filtrado = df[
    df["edad"].between(edades[0], edades[1])
]

st.dataframe(filtrado, use_container_width=True)

st.subheader("Distribución de diabetes")

conteo = df["diabetes"].value_counts().reindex(
    [0, 1], fill_value=0
)

st.bar_chart(conteo.rename(index={
    0: "Sin diabetes",
    1: "Con diabetes"
}))
