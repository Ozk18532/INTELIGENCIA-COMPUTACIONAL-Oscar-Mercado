import streamlit as st
from PIL import Image
import numpy as np

# =============================
# Configuración de página
# =============================
st.set_page_config(
    page_title="Clasificador Perro vs Gato",
    page_icon="🐶🐱",
    layout="centered"
)

# =============================
# Fondo personalizado + estilos
# =============================
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
}

.main-card {
    background-color: white;
    padding: 2rem;
    border-radius: 20px;
    box-shadow: 0px 10px 30px rgba(0,0,0,0.15);
}

.title-style {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #ff4b4b;
}

.subtitle-style {
    text-align: center;
    font-size: 18px;
    color: #555;
}
</style>
""", unsafe_allow_html=True)

# =============================
# Tarjeta central
# =============================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="title-style">🐶🐱 Clasificador Perro vs Gato</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-style">Sube una imagen y descubre qué animal es 🧠✨</div>', unsafe_allow_html=True)

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
        predict_btn = st.button("Predecir 🚀")

    if predict_btn:
        if demo_mode:
            st.info("⚠️ Aún no se cargó el modelo entrenado. Esto es solo demostración visual.")
            st.success("Predicción simulada: **Dog 🐶**")
        else:
            st.error("Modelo no cargado todavía.")

else:
    st.caption("Tip: usa una foto clara donde se vea bien el animal 📸")

st.markdown('</div>', unsafe_allow_html=True)

