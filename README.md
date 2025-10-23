🥗 Generador de Plan Alimenticio con IA

Aplicación interactiva construida con Streamlit que utiliza la API de modelos de GitHub para generar planes alimenticios semanales personalizados basados en el objetivo del usuario (pérdida de grasa, ganancia muscular o mantenimiento) y sus restricciones dietéticas.

✨ Características

Generación por IA: Utiliza el modelo gpt-4o-mini (configurable) a través de la infraestructura de GitHub para crear planes.

Personalización: Adaptación del plan según nombre, edad, peso, objetivo y restricciones.

Interfaz Simple: Aplicación web sencilla gracias a Streamlit.

⚙️ Configuración del Entorno Local

Para ejecutar esta aplicación en tu máquina, sigue estos pasos:

1. Clonar el Repositorio

Dado que ya subiste el código, simplemente trabaja en tu carpeta local. Si alguien más quisiera clonarlo, usaría:

git clone [https://github.com/JMarvinMora/plan-alimenticio-ia.git](https://github.com/JMarvinMora/plan-alimenticio-ia.git)
cd plan-alimenticio-ia


2. Crear Entorno Virtual (Recomendado)

Crea y activa un entorno virtual para aislar las dependencias:

# Crear entorno virtual (solo la primera vez)
python -m venv .venv

# Activar el entorno (Windows)
.\.venv\Scripts\activate

# Activar el entorno (macOS/Linux)
source ./.venv/bin/activate


3. Instalar Dependencias

Instala todas las librerías necesarias listadas en requirements.txt:

pip install -r requirements.txt


4. Configurar Variables de Entorno

La aplicación requiere un token de acceso para la API de GitHub.

Copia el archivo de ejemplo a tu archivo de configuración secreto:

copy .env.example .env
# O en Linux/macOS: cp .env.example .env


Edita el archivo .env y reemplaza your_token_here con tu [Personal Access Token de GitHub] que tenga permisos para usar los modelos de IA.

Contenido de .env (tras la edición):

API_HOST=github
GITHUB_TOKEN=ghp_TU_TOKEN_REAL_AQUI
GITHUB_MODEL=gpt-4o-mini


5. Ejecutar la Aplicación

Con el entorno activado y el .env configurado, inicia la aplicación Streamlit:

streamlit run app.py


Esto abrirá la aplicación en tu navegador (generalmente en http://localhost:8501).

📁 Estructura del Proyecto

app.py: Lógica principal de la aplicación Streamlit y manejo de la API de IA.

requirements.txt: Lista de librerías Python necesarias.

.env.example: Plantilla pública para la configuración de variables de entorno.

.gitignore: Lista de archivos ignorados (vital para excluir .env y .venv).

⌨️ con  por JMarvinMora