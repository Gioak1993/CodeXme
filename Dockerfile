# FROM python:3.11

# WORKDIR /app
# COPY . .

# ENV VIRTUAL_ENV=/app/.venv_docker
# ENV PATH="$VIRTUAL_ENV/bin:$PATH"
# RUN python3.11 -m venv $VIRTUAL_ENV

# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r requirements.txt

# CMD reflex run --env prod


FROM python:3.11

# Configura el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el contenido del proyecto al contenedor
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3.11 -m venv $VIRTUAL_ENV

RUN pip install  --upgrade pip

# Instala las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Inicializa la app y descarga las dependencias de npm
RUN reflex init

# Compila el frontend
RUN reflex export --frontend-only --no-zip

# Aplica migraciones y ejecuta la app en modo producción
CMD [ -d alembic ] && reflex db migrate; reflex run --env prod