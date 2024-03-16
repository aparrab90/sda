FROM python:3.8-slim
WORKDIR /app
COPY . .
# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt
# CMD para ejecutar la aplicación
CMD ["python", "embassador.py"]
