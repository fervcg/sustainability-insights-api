from fastapi import FastAPI, UploadFile, File
import pandas as pd
import io

app = FastAPI(
    title="Sustainability Insights API",
    description="API para procesar y analizar métricas de impacto ambiental."
)

# Creamos una "base de datos" temporal en la memoria para guardar los cálculos
db_emisiones = []

@app.get("/")
def read_root():
    return {"status": "Online", "message": "¡Bienvenida a la Sustainability Insights API!"}

# --- NUEVO ENDPOINT: Para subir y procesar datos ---
@app.post("/procesar-consumo")
async def procesar_consumo(file: UploadFile = File(...)):
    # 1. Leer el archivo que suba el usuario
    contenido = await file.read()
    
    # 2. Usar Pandas para transformar ese archivo en una tabla interactiva (DataFrame)
    # Forzamos la decodificación ignorando errores de caracteres extraños
    contenido_decodificado = contenido.decode('utf-8', errors='replace')
    df = pd.read_csv(io.StringIO(contenido_decodificado))
    
    # 3. LÓGICA AMBIENTAL: Calcular CO2 (Ejemplo: 1 litro de diésel = 2.68 kg de CO2)
    # Pandas multiplica toda la columna entera en una fracción de segundo
    df['co2_emitido_kg'] = df['litros_consumidos'] * 2.68
    
    # 4. Guardar los resultados en nuestra base de datos temporal
    registros = df.to_dict(orient="records")
    db_emisiones.extend(registros)
    
    # 5. Devolver un resumen de lo que se procesó
    return {
        "mensaje": "Archivo procesado con éxito",
        "filas_leidas": len(df),
        "total_co2_kg_calculado": df['co2_emitido_kg'].sum()
    }

# --- NUEVO ENDPOINT: Para consultar el resumen general ---
@app.get("/metricas/resumen")
def obtener_resumen():
    if not db_emisiones:
        return {"alerta": "Aún no se han procesado datos."}
    
    # Convertimos los datos guardados de vuelta a una tabla de Pandas para calcular fácil
    df_total = pd.DataFrame(db_emisiones)
    
    return {
        "total_historico_co2_kg": df_total['co2_emitido_kg'].sum(),
        "promedio_co2_por_viaje": df_total['co2_emitido_kg'].mean(),
        "vehiculos_analizados": len(df_total)
    }

