import streamlit as st
import os
from dotenv import load_dotenv
import openai

# Cargar variables de entorno
load_dotenv(override=True)

# Configurar cliente de IA (usando GitHub Models)
client = openai.OpenAI(
    base_url="https://models.github.ai/inference",
    api_key=os.environ["GITHUB_TOKEN"]
)
MODEL_NAME = os.getenv("GITHUB_MODEL", "openai/gpt-4o-mini")

# Configurar la página
st.set_page_config(
    page_title="Plan Alimenticio con IA 🍎",
    page_icon="🥦",
    layout="centered"
)

st.title("🥗 Generador de Plan Alimenticio con IA")
st.write("Ingresa tus datos y obtén un plan alimenticio personalizado creado por inteligencia artificial.")

# Formulario de entrada
with st.form("plan_form"):
    nombre = st.text_input("Tu nombre")
    edad = st.number_input("Edad", min_value=1, max_value=120, value=30)
    peso = st.number_input("Peso (kg)", min_value=30.0, max_value=200.0, value=70.0)
    objetivo = st.selectbox("Objetivo", ["bajar grasa", "ganar músculo", "mantener peso"])
    restricciones = st.text_input("Restricciones alimenticias (opcional)", placeholder="Ej. sin gluten, vegetariano...")
    generar = st.form_submit_button("Generar plan 🧠")

if generar:
    with st.spinner("Generando tu plan alimenticio... 🍽️"):
        prompt = f"""
        Eres un nutricionista experto. Crea un plan alimenticio semanal personalizado.
        Datos del usuario:
        - Nombre: {nombre}
        - Edad: {edad}
        - Peso: {peso} kg
        - Objetivo: {objetivo}
        - Restricciones: {restricciones}

        Incluye comidas por día (desayuno, almuerzo, cena y snacks),
        con porciones aproximadas y consejos saludables.
        """

        try:
            response = client.chat.completions.create(
                model=MODEL_NAME,
                temperature=0.8,
                messages=[
                    {"role": "system", "content": "Eres un asistente experto en nutrición que crea planes alimenticios equilibrados y variados."},
                    {"role": "user", "content": prompt}
                ]
            )

            st.success("✅ Plan generado con éxito")
            st.markdown(response.choices[0].message.content)

        except Exception as e:
            st.error(f"⚠️ Error al generar el plan: {e}")
