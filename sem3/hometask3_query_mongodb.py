'''
Поэкспериментируйте с различными методами запросов.
'''

import json
from pymongo import MongoClient
import re

client = MongoClient("mongodb://localhost:27017/")

db = client['db_books']
books = db['books_data']

books_data = books.find()

for item in books_data:
    #print(item['title'])
    break

count_books = books.count_documents({})
print(f'Общее количество книг - {count_books}')

query = {"availability": 20}
print(f'Количетво книг с наличием 20 шт. - {books.count_documents(query)}')

projection = {"_id": 0, "title": 1, "availability": 1}
for item in books.find(query, projection):
    print(item)

availability_lt_20_count = books.count_documents({"availability": {"$lt": 20}})
availability_gte_20_count = books.count_documents({"availability": {"$gte": 20}})
print("Количество книг, которых в наличии меньше 20:", availability_lt_20_count)
print("Количество книг, которых в наличии от 20:", availability_gte_20_count)

print(f"Количество книг со словом 'little' без учета регистра - {books.count_documents({'description' : {'$regex' : '[Ll]ittle'}})}")
print(f"Количество книг со словом 'little' с учетом регистра - {books.count_documents({'description' : {'$regex' : '[l]ittle'}})}")

print(f"Количество книг, которых в наличии или 19, или 20 - {books.count_documents({'availability' : {'$in' : [19, 20]}})}")

print(f"Количество книг, в описании которых есть слова или 'little', или 'big' - {books.count_documents({'description' : {'$in': [ re.compile('.*big.*'), re.compile('.*little.*')]}})}")

print(f"Количество книг, в описании которых есть слова и 'little', и 'big' - {books.count_documents({'description' : {'$all': [ re.compile('.*big.*'), re.compile('.*little.*')]}})}")

print(f"Количество книг с названием не 'Libertarianism for Beginners' - {books.count_documents({'title' : {'$ne' : 'Libertarianism for Beginners'}})}")