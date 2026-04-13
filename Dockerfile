# 1. Traer Python 3.10 
FROM python:3.10-slim

# 2. Crear una carpeta llamada /app dentro de ese computador de Google
WORKDIR /app

# 3. Copiar nuestra lista de empaque desde tu PC hacia Google
COPY requirements.txt .

# 4. Google trae la lista e instala las herramientas
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar código (main.py) hacia la carpeta de Google
COPY . .

# 6. La instrucción final: "Cuando te enciendas, arranca Uvicorn"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
