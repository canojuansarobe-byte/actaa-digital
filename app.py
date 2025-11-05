import streamlit as st
import hashlib
import time
import json
from datetime import datetime

st.set_page_config(page_title="Acta Digital", page_icon="📄")

st.title("📄 Acta Digital")
st.markdown("Sistema de registro inmutable de actas")

# Función para calcular hash
def calcular_hash(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

# Interfaz principal
with st.form("form_acta"):
    titulo = st.text_input("Título del acta")
    contenido = st.text_area("Contenido del acta", height=200)
    participantes = st.text_input("Participantes (separados por coma)")
    
    if st.form_submit_button("📌 Registrar Acta"):
        if titulo and contenido:
            # Crear registro
            timestamp = time.time()
            fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            acta = {
                "titulo": titulo,
                "contenido": contenido,
                "participantes": [p.strip() for p in participantes.split(",")],
                "fecha": fecha,
                "timestamp": timestamp,
                "hash": calcular_hash(f"{titulo}{contenido}{timestamp}")
            }
            
            st.success("✅ Acta registrada correctamente")
            st.json(acta)
            
            # Mostrar hash
            st.info(f"**Hash único:** `{acta['hash']}`")
        else:
            st.error("❌ Completa título y contenido")

st.markdown("---")
st.caption("Cada acta genera un hash único que certifica su integridad")
