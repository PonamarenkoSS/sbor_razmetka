'''
Выполнить скрейпинг данных в веб-сайта http://books.toscrape.com/ и извлечь информацию о всех 
книгах на сайте во всех категориях: название, цену, количество товара в наличии 
(In stock (19 available)) в формате integer, описание.
Затем сохранить эту информацию в JSON-файле.
'''

import requests
from bs4 import BeautifulSoup
import urllib.parse
from datetime import datetime, time, timedelta
import time
import re
import json
import pandas as pd

base_url_for_page_2 = 'http://books.toscrape.com/'
base_url_for_other_page = 'http://books.toscrape.com/catalogue/'
url = 'http://books.toscrape.com/'

url_list = []
number_page = 0

while True:
    number_page += 1
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    next_page_link = soup.find('li', ('class', 'next'))
    for link in soup.find_all('li', ('class', 'col-xs-6 col-sm-4 col-md-3 col-lg-3')):
        if link.find('a'):
            url_list.append(link.find('a').get('href'))
    
    if not next_page_link:
        break
    
    if number_page == 1:
        url = base_url_for_page_2 + next_page_link.find('a')['href']
    else:
        url = base_url_for_other_page + next_page_link.find('a')['href']


url_joined = []

for link in url_list:
  url_joined.append(urllib.parse.urljoin('http://books.toscrape.com/catalogue/', link.replace('catalogue/', '')))

data = []
number = 0
for url in url_joined:
    number += 1
    print(number, url)
    response = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('article', {'class': 'product_page'})
    row_data = {}
    try: 
        title = table.find('h1').text
    except KeyError:
        title = ''
    try:
        price = float(table.find('p', {'class': 'price_color'}).text.replace('£', '').replace(',', '.'))
    except KeyError:
        price = ''
    try: 
        availability = int(''.join([i for i in table.find('p', {'class', 'instock availability'}).text if i.isdigit()]))
    except KeyError:
        availability = ''
    try:
        description = table.find_all('p')[3].text.strip()
    except KeyError:
        description = ''
 
    row_data = {'title': title, 'price': price, 'availability': availability, 'description': description}
    data.append(row_data)
    time.sleep(10)


df = pd.DataFrame(data)
print(df.head())
print(len(df))

with open('booksdata.json', 'w') as f:
    json.dump(data, f)
