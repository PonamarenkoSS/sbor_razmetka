'''
Выберите веб-сайт с табличными данными, который вас интересует.
Напишите код Python, использующий библиотеку requests для отправки HTTP GET-запроса 
на сайт и получения HTML-содержимого страницы.
Выполните парсинг содержимого HTML с помощью библиотеки lxml, чтобы извлечь данные из таблицы.
Сохраните извлеченные данные в CSV-файл с помощью модуля csv.

Ваш код должен включать следующее:

Строку агента пользователя в заголовке HTTP-запроса, чтобы имитировать веб-браузер и избежать блокировки сервером.
Выражения XPath для выбора элементов данных таблицы и извлечения их содержимого.
Обработка ошибок для случаев, когда данные не имеют ожидаемого формата.
Комментарии для объяснения цели и логики кода.

Примечание: Пожалуйста, не забывайте соблюдать этические и юридические нормы при веб-скреппинге.
'''

import requests
from lxml import html
from pymongo import MongoClient
import pandas as pd
import datetime
import time

url = 'https://cbr.ru/currency_base/daily/'

response = requests.get(url, headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'})

tree = html.fromstring(response.content)

result = []

rows = tree.xpath('//*[@id="content"]/div/div/div/div[3]/div/table/tbody')

headers = rows[0].xpath("./tr[1]/th/text()")
print(f'{headers=}')

result = []

for i in range(2, 45): # исходя из разметки сайта данные таблицы хранятся в теге tr с 2 до 44
  data = {}
  for el, dict_el in zip(rows[0].xpath(f".//tr[{i}]/td/text()"), headers):
      if dict_el == 'Единиц':
        try: 
          data[dict_el] = int(el.strip())
        except KeyError:
          data[dict_el] = '-'
      elif dict_el == 'Курс':
        try:
          data[dict_el] = float(el.strip().replace(',', '.'))
        except KeyError:
          data[dict_el] = '-'
      else:
        try:
          data[dict_el] = el.strip()
        except KeyError:
          data[dict_el] = '-'
  print(f'{data=}')
  result.append(data)

print(f'Первая строка - {result[0]}')

df = pd.DataFrame(result)
df.to_csv('kurs_valut_result.csv', index=False)