FROM python:3.11-slim

# Evitar la escritura de pyc y forzar salida sin buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copiar el resto del código
COPY . /app

# Puerto no necesario pero documentado
EXPOSE 80

# Entrypoint
CMD ["python", "bot.py"]
