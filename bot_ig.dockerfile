# Usamos una imagen base específica con la última versión de Python
FROM python:3.8

# Etiqueta de información del creador
LABEL maintainer="valsayesech@gmail.com"

# Instalamos las dependencias específicas de tu aplicación, si es necesario
RUN apt-get update && apt-get install -y \
    software-properties-common

# Copiamos los archivos necesarios al contenedor
COPY adap_img2.py /app/

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requisitos e instalamos las dependencias de Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Comando a ejecutar cuando se inicie un contenedor basado en esta imagen
CMD ["python", "adap_img2.py"]
