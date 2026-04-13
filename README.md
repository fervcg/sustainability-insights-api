# Sustainability Insights API

API RESTful serverless diseñada para ingestar, procesar y analizar métricas de impacto ambiental y huella de carbono a partir de datos de consumo energético en flotas vehiculares o procesos industriales.

Este proyecto demuestra la integración de conocimientos de ingeniería ambiental con desarrollo backend moderno, permitiendo transformar datos operacionales en métricas accionables para la toma de decisiones.

---

## Objetivo del Proyecto

Desarrollar una solución backend capaz de procesar datos de consumo energético y generar indicadores ambientales relevantes, utilizando tecnologías modernas de desarrollo y despliegue en la nube.

---

## Live Demo

La API se encuentra desplegada en Google Cloud Run y es accesible públicamente:

https://sustainability-api-178920735458.southamerica-west1.run.app/docs

---

## Stack Tecnológico

- Lenguaje: Python 3.10  
- Framework: FastAPI (ejecutado con Uvicorn)  
- Procesamiento de datos: Pandas  
- Contenerización: Docker  
- Cloud Provider: Google Cloud Platform (Cloud Run)  

---

## Arquitectura y Flujo de Datos

1. **Ingesta**  
   El sistema recibe archivos `.csv` mediante un endpoint HTTP `POST`.

2. **Procesamiento**  
   Los datos son decodificados y transformados utilizando Pandas. Se aplican factores de emisión para calcular la cantidad de CO2 emitido a partir del consumo registrado.

3. **Persistencia (Temporal)**  
   Los resultados se almacenan en memoria (in-memory storage), simulando una base de datos para fines demostrativos.

4. **Reporte**  
   Un endpoint `GET` permite consultar métricas agregadas, como emisiones totales, promedios y cantidad de registros procesados.

## Consideraciones sobre el Cálculo de Emisiones

El factor de emisión utilizado (2,68 kg CO₂ por litro de combustible) corresponde únicamente a las emisiones directas de dióxido de carbono (CO₂) generadas por la combustión.

Este cálculo no incluye otros gases de efecto invernadero ni emisiones asociadas al ciclo de vida del combustible.

### Alcance del cálculo

- Incluye:
  - Emisiones directas de CO₂ por combustión

- No incluye:
  - Emisiones de CH₄ (metano)
  - Emisiones de N₂O (óxido nitroso)
  - Emisiones asociadas a extracción, refinación y transporte del combustible

Por lo tanto, los resultados representan emisiones de CO₂ directo y no el equivalente total de carbono (CO₂e) del ciclo de vida completo.
---

## Endpoints

### POST /procesar-consumo

Procesa un archivo CSV con datos de consumo energético.

- Input: archivo `.csv` (multipart/form-data)  
- Output: JSON con resumen del procesamiento  

### GET /metricas/resumen

Devuelve métricas agregadas a partir de los datos procesados.

- Output: JSON con:
  - total histórico de CO2  
  - promedio de emisiones  
  - cantidad de registros  

---

## Ejemplo de Input 

```csv
id_vehiculo,litros_consumidos
CAMION-001,150
CAMION-002,200

## Ejemplo de Output

{
  "filas_leidas": 2,
  "total_co2_kg_calculado": 938
}

---

## Ejecución Local
1. Clonar el repositorio:
git clone https://github.com/fervcg/sustainability-insights-api.git
cd sustainability-insights-api

2. Crear y activar entorno virtual:
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar servidor:
uvicorn main:app --reload

5. Acceder a la documentación interactiva:
http://127.0.0.1:8000/docs

---

Limitaciones
La persistencia es temporal; los datos se pierden al reiniciar el servicio.
No se implementa autenticación ni control de acceso.
El sistema está orientado a demostración y no a uso productivo a gran escala.

---

Consideraciones Técnicas
La solución fue desplegada utilizando una arquitectura serverless en Google Cloud Run, lo que permite escalar automáticamente según la demanda y optimizar el uso de recursos.
El uso de FastAPI facilita la creación de APIs de alto rendimiento con validación automática de datos y documentación integrada.
