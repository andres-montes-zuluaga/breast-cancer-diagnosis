# breast-cancer-diagnosis
Breast cancer diagnosis with Perceptron

# Diagnóstico de Cáncer de Mama con el Perceptrón

> Proyecto de clasificación utilizando un modelo de perceptrón y el dataset [**Breast Cancer Wisconsin (Diagnostic)**](https://archive.ics.uci.edu/dataset/17/breast+cancer+wisconsin+diagnostic) del UCI Machine Learning Repository.

---

## Índice

- [Descripción](#descripción)
- [Capturas de Pantalla / Demo](#capturas-de-pantalla--demo)
- [Características Principales](#características-principales)
- [Requisitos Previos](#requisitos-previos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Configuración](#configuración)
- [Contribución](#contribución)
- [Licencia](#licencia)
- [Autores y Créditos](#autores-y-créditos)
- [Contacto](#contacto)

---

## Descripción

Este proyecto implementa un modelo de **perceptrón** para el diagnóstico de cáncer de mama. Se utiliza el dataset **Breast Cancer Wisconsin (Diagnostic)**, y se desarrolló empleando Python y bibliotecas como **NumPy**, **pandas**, **matplotlib** y **scikit-learn**. La meta es clasificar correctamente entre casos benignos y malignos a partir de características extraídas de los datos.

---

## Capturas de Pantalla / Demo

Si deseas incluir imágenes o GIFs que demuestren el funcionamiento del modelo, puedes hacerlo de la siguiente forma:

```markdown
![Demo del Notebook](ruta/a/tu_imagen.png)

---

## Características Principales
- Implementación del Perceptrón: Algoritmo de clasificación binaria.
- Preprocesamiento de Datos: Análisis exploratorio, limpieza y normalización.
- Evaluación del Modelo: Cálculo y visualización de métricas de rendimiento, como precisión y recall.
- Visualizaciones Interactivas: Gráficos y diagramas que facilitan la interpretación de resultados.
Nota: Estos elementos aseguran que el proyecto sea comprensible y reproducible.

---

## Requisitos Previos
Antes de instalar el proyecto, asegúrate de tener instaladas las siguientes herramientas:

Herramienta	    Versión Mínima
Python	            3.7
NumPy	            1.18
pandas	            1.0
matplotlib	        3.0
scikit-learn	    0.22
Jupyter Notebook	-

Recomendación: Usa un entorno virtual para evitar conflictos entre dependencias.

---

## Instalación
Sigue estos pasos para configurar el proyecto en tu máquina:

1. **Clonar el repositorio**:
**Abrir Git bash**
git clone https://github.com/usuario/diagnostico-cancer-perceptron.git

2. **Acceder al directorio del proyecto**:
**Abrir Git bash**
cd diagnostico-cancer-perceptron

3. **Crear y activar un entorno virtual** (opcional, pero recomendado):
- Linux/Mac:
Abrir Git bash
python3 -m venv env
source env/bin/activate

- Windows:
Abrir Git bash
python -m venv env
env\Scripts\activate

4. **Instalar las dependencias**:
Abrir Git bash
pip install -r requirements.txt

---

## Uso
Para ejecutar el análisis y entrenamiento del modelo...

---

## Configuración
Puedes personalizar algunos aspectos del proyecto:

Parámetros del Perceptrón: Modifica la tasa de aprendizaje y el número de iteraciones en el notebook.
Ruta del Dataset: Cambia la ruta si deseas utilizar otro conjunto de datos.

En Python:
# Ejemplo de configuración en el notebook
LEARNING_RATE = 0.01
NUM_ITERATIONS = 1000
DATASET_PATH = "ruta/al/dataset.csv"

---

## Contribución
¡Las contribuciones son bienvenidas! Sigue estos pasos para colaborar:
1. Fork este repositorio.
2. Crea una rama para tu cambio:
Abre Git bash
git checkout -b feature/nueva-funcionalidad
3. Realiza tus cambios y haz un commit:
Abre Git bash
git commit -am "Añadida nueva funcionalidad"
4. Envía un Pull Request con una descripción detallada de tus cambios.

Recordatorio: Asegúrate de seguir las directrices de contribución para mantener la coherencia del proyecto.

---

## License
This project is licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/). To view a copy of this license, visit [this link](https://creativecommons.org/licenses/by-nc/4.0/legalcode).

---

## Autores y Créditos
- Andrés MONTES ZULUAGA – Desarrollador principal.
- Inspirado en el dataset del UCI Machine Learning Repository.

---

## Contacto
Para dudas o consultas, puedes contactarme a través de:
andres.montes-zuluaga@laplateforme.io