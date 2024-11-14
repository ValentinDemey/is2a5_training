
import os

# Accéder aux variables d'environnement
db_url = os.getenv("DATABASE_URL_1", "default_url")
print("Database URL:", db_url)
