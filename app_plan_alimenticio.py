import streamlit as st
import os
from dotenv import load_dotenv
import openai

# --- CONFIGURACIÓN INICIAL ---

# Cargar variables de entorno desde el archivo .env
# La línea "\Scripts\activate" se ha eliminado porque NO es código Python.
load_dotenv(override=True)

# Configurar cliente de IA (usando GitHub Models)
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ.get("GITHUB_TOKEN")
)

MODEL_NAME = os.environ.get("GITHUB_MODEL", "openai/gpt-4o-mini")

# --- CONFIGURACIÓN DE PÁGINA DE STREAMLIT ---

st.set_page_config(
    page_title="Plan Alimenticio con IA 🍎",
    page_icon="🥦",
    layout="centered"
)

st.title("🥗 Generador de Plan Alimenticio con IA")
st.write("Ingresa tus datos y obtén un plan alimenticio personalizado creado por inteligencia artificial.")

# --- FORMULARIO DE ENTRADA ---

with st.form("plan_form"):
    nombre = st.text_input("Tu nombre")
    edad = st.number_input("Edad", min_value=1, max_value=120, value=30)
    peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
    objetivo = st.selectbox("Objetivo", ["bajar grasa", "ganar músculo", "mantener peso"])
    restricciones = st.text_input("Restricciones alimenticias (opcional)", placeholder="Ej. sin gluten, vegetariano...")
    generar = st.form_submit_button("Generar plan 🧠")

# --- LÓGICA DE GENERACIÓN DE PLAN ---

if generar:
    # Verificación de que el token esté disponible
    if not os.environ.get("GITHUB_TOKEN"):
        st.error("⚠️ Error de configuración: El GITHUB_TOKEN no está configurado.")
    else:
        with st.spinner("Generando tu plan alimenticio... 🍽️"):
            prompt = f"""
            Eres un nutricionista experto. Crea un plan alimenticio semanal personalizado.
            Datos del usuario:
            - Nombre: {nombre if nombre else 'Usuario'}
            - Edad: {edad}
            - Peso: {peso} kg
            - Objetivo: {objetivo}
            - Restricciones: {restricciones if restricciones else 'Ninguna'}

            Incluye comidas por día (desayuno, almuerzo, cena y snacks),
            con porciones aproximadas y consejos saludables. Responde en formato Markdown, bien estructurado.
            """

            try:
                # Llamada a la API de modelos de GitHub
                response = client.chat.completions.create(
                    model=MODEL_NAME,
                    temperature=0.8,
                    messages=[
                        {"role": "system", "content": "Eres un asistente experto en nutrición que crea planes alimenticios equilibrados y variados, utilizando un lenguaje amigable y profesional. La respuesta debe ser un plan semanal completo en formato Markdown."},
                        {"role": "user", "content": prompt}
                    ]
                )

                st.success("✅ Plan generado con éxito")
                st.markdown(response.choices[0].message.content)

            except Exception as e:
                # Manejo de errores de la API
                st.error(f"⚠️ Error al generar el plan. Asegúrate de que el token y el modelo sean correctos. Error: {e}")
