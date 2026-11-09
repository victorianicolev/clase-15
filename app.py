
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(
    page_title="Mi primera aplicación de Streamlit",
    page_icon="🎓",
    layout="wide"
)

# --- Título principal ---
st.title("Mi primera aplicación de Streamlit")

# --- Área principal ---
st.header("¡Hola! Bienvenido a mi aplicación 👋")

st.write(
    "Esta aplicación permite ingresar mensajes, "
    "presionar botones e interactuar con Streamlit."
)

# --- Logo institucional ---
st.subheader("Logo institucional")

try:
    st.image("logo.png", width=180)
except:
    st.info("Agrega el logo institucional en la carpeta del proyecto.")

# --- Botón principal ---
st.subheader("Interacción principal")

if st.button("Haz clic"):
    st.success("¡El botón principal fue presionado!")

# --- Campo de texto principal ---
mensaje_principal = st.text_input(
    "Escribe algo",
    key="texto_principal"
)

if mensaje_principal:
    st.write("Escribiste:", mensaje_principal)
else:
    st.info("Por favor, escribe un mensaje.")

# ==========================================
# BARRA LATERAL
# ==========================================

st.sidebar.header("Mi primera barra lateral de Streamlit")

st.sidebar.write(
    "¡Hola! Bienvenido a la barra lateral. "
    "Aquí puedes realizar otras interacciones."
)

# --- Logo en barra lateral ---
try:
    st.sidebar.image("logo.png", width=150)
except:
    st.sidebar.info("Agrega el logo institucional.")

# --- Botón lateral ---
st.sidebar.subheader("Interacción lateral")

if st.sidebar.button("Haz clic aquí"):
    st.sidebar.success("¡El botón lateral fue presionado!")

# --- Campo de texto lateral ---
mensaje_lateral = st.sidebar.text_input(
    "Escribe algo en la barra",
    key="texto_lateral"
)

if mensaje_lateral:
    st.sidebar.write("Escribiste:", mensaje_lateral)
else:
    st.sidebar.info("Por favor, escribe un mensaje.")
