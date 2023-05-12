# Utilisation de l'image Python 3.9 comme base
FROM python:3.9

# Copie du code dans l'image
COPY . /app
WORKDIR /app

# Installation des dépendances
RUN pip install --no-cache-dir nameko nameko-sqlalchemy psycopg2-binary

# Exposition du port 8000
EXPOSE 8001

