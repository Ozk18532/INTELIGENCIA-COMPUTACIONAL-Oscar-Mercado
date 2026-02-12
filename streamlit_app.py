import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(page_title="Clasificador Perro vs Gato", page_icon="🐶🐱", layout="centered")

st.title("Clasificador Perro vs Gato 🐶🐱")
st.write("Sube una imagen y la app mostrará la predicción. (Por ahora: interfaz + demo visual)")

st.divider()

uploaded_file = st.file_uploader("Selecciona una imagen (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Imagen cargada", use_container_width=True)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        demo_mode = st.toggle("Modo demo (sin modelo)", value=True)

    with col2:
        predict_btn = st.button("Predecir")

    if predict_btn:
        if demo_mode:
            st.info("⚠️ Aún no se cargó el modelo entrenado. Esto es solo demo visual.")
            st.write("Resultado simulado:")
            st.success("Predicción: **Dog** (confianza simulada: 0.75)")
        else:
            st.error("Todavía no hay modelo cargado. Activa 'Modo demo' o agrega el modelo.")
else:
    st.caption("Tip: usa una foto clara donde se vea bien el animal.")
