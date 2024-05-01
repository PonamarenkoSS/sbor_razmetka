'''
Установите MongoDB на локальной машине, а также зарегистрируйтесь в онлайн-сервисе. 
https://www.mongodb.com/ https://www.mongodb.com/products/compass
Загрузите данные который вы получили на предыдущем уроке путем скрейпинга сайта с помощью Buautiful Soup 
в MongoDB и создайте базу данных и коллекции для их хранения.
'''

import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")

db = client['db_books']
books = db['books_data']

with open('/Users/svetlanaponamarenko/Desktop/Python/сбор/sem3/booksdata.json', 'r') as file:
    books_json = json.load(file)

books.insert_many(books_json)