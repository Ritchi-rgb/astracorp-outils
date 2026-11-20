# Image de départ : un Linux minimal avec Python 3.12 déjà installé
FROM python:3.12-slim

# Le dossier de travail dans l'image (créé s'il n'existe pas), comme un cd
WORKDIR /app

# D'abord la liste des dépendances, puis leur installation
COPY requirements-dev.txt .
RUN pip install --no-cache-dir -r requirements-dev.txt

# Ensuite le code
# À COMPLÉTER : copier tout le dossier courant dans l'image

# La commande lancée au démarrage d'un conteneur
# À COMPLÉTER : lancer pytest en mode verbeux
