#pip install python-dotenv

from dotenv import load_dotenv
import os

load_dotenv()

# Accéder aux variables d'environnement
db_url = os.getenv("DATABASE_URL", "default_url")
print("Database URL:", db_url)
