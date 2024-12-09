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

while crawler_ongoing and page_number<=MAX_PAGE:
    logging.info(f'page nb : {str(page_number)}')
    crawler_url = f'{COMMON_URL}/page-{page_number}.html'
    webpage = requests.get(crawler_url, headers=HEADERS) 
    soup = BeautifulSoup(webpage.content, "html.parser") 
    dom = etree.HTML(str(soup)) 

    elements = dom.xpath('//*[@id="default"]/div/div/div/div/section/div[2]/ol/li[*]/article/h3/a')
    if len(elements)>0:
        for element in elements:
            book_urls.append(element.get('href'))
        page_number+=1
        time.sleep(0.1)
    else :
        crawler_ongoing=False

### PARSER
logging.info(f'STARTING TO PARSE')

def get_text_element_from_xpath(xpath):
    try:
        return dom.xpath(xpath)[0].text
    except:
        return ''

book_data=[]

for i,book_url in enumerate(book_urls):
    logging.info(f'PARSING {i}/{len(book_urls)}')
    parser_url = f"{COMMON_URL}{book_url}"
    webpage = requests.get(parser_url, headers=HEADERS) 
    soup = BeautifulSoup(webpage.content, "html.parser") 
    dom = etree.HTML(str(soup))

    book_name = get_text_element_from_xpath('//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    book_description = get_text_element_from_xpath('//article/p')
    book_price = get_text_element_from_xpath('//tr[3]/td')
    book_price=float(book_price.replace('£',''))
    book_data.append(
        {   'technical_uuid': str(uuid.uuid4()),
            'book_name':book_name,
            'description':book_description,
            'price':str(book_price),
        }
    )
    time.sleep(0.1)


### EXPORT DATA TO CSV
logging.info(f'LOADING DATA INTO {OUTPUT_FILENAME}')
with open(OUTPUT_FILENAME, "w", newline="", encoding='utf-8') as csvfile:
    champs = ["technical_uuid","book_name", "description", "price"] 
    writer = csv.DictWriter(csvfile, fieldnames=champs)

    writer.writeheader()
    writer.writerows(book_data)