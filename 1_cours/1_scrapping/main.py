from bs4 import BeautifulSoup 
from lxml import etree 
import requests 
import time
import csv
import logging
import uuid

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

COMMON_URL='https://books.toscrape.com/catalogue/'
HEADERS=({'User-Agent': 
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36','Accept-Language': 
            'en-US, en;q=0.5'})
MAX_PAGE=1
OUTPUT_FILENAME='fichier.csv'

### CRAWLER
logging.info(f'STARTING TO CRAWLE')
crawler_ongoing=True
page_number=1
book_urls=[]
   
    # TODO : compléter le code du crawler
    # le crawler alimente la liste book_urls avec les pages des livres
    # le crawler continue de parcourir le site tant qu'il y a encore des livres dans la page

### PARSER
logging.info(f'STARTING TO PARSE')

# TODO : compléter le code du parser pour extraire certaines informations de la page livre


### EXPORT DATA TO CSV
logging.info(f'LOADING DATA INTO {OUTPUT_FILENAME}')
# TODO : compléter le code permettant l'export dans un fichier