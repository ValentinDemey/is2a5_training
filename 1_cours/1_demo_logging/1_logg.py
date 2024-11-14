import logging

# Configuration basique du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemple de logs
logging.debug("Ceci est un message DEBUG")
logging.info("Ceci est un message INFO")
logging.warning("Ceci est un message WARNING")
logging.error("Ceci est un message ERROR")
logging.critical("Ceci est un message CRITICAL")
