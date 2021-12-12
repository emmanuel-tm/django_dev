FROM python:3.10.0
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /opt/back_end
COPY . /opt/back_end
# Agrego una variable de entorno con el
# nombre de la Base de Datos, ya que voy a 
# trabajar con SQLite.
ENV SQLITE_DB=django_dev.db
