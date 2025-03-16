# Usa una imagen de Python con compatibilidad con PyTorch
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos
COPY . .

# Expone el puerto en el contenedor
EXPOSE 8080

# Comando para iniciar la app con Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
