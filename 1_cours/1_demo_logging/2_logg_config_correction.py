import logging

# Configuration avancée du logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Écriture dans la console
        logging.FileHandler('app.log', mode='a')  # Écriture dans un fichier en mode append
    ]
)

# Exemple de logs
logging.info("Ce message sera affiché dans la console et écrit dans le fichier app.log")
logging.warning("Ceci est un message WARNING")
