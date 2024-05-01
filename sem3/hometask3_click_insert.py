'''
Зарегистрируйтесь в ClickHouse.
Загрузите данные в ClickHouse и создайте таблицу для их хранения.
'''

from clickhouse_driver import Client
import json

client = Client('localhost')

client.execute('CREATE DATABASE IF NOT EXISTS db_books')

client.execute('''
CREATE TABLE IF NOT EXISTS db_books.books (
id Int64,
title String,
price Float64,
availability Int64,
description String
) ENGINE = MergeTree()
ORDER BY id
''')

print("Таблица создана успешно.")

with open('/Users/svetlanaponamarenko/Desktop/Python/сбор/sem3/booksdata.json', 'r') as file:
    data = json.load(file)

id = 1
for feature in data:
    feature['id'] = id
    id += 1

for feature in data:
    client.execute("""
    INSERT INTO db_books.books (
    id, title, price, availability, description
    ) VALUES""",
    [(feature['id'],
    feature['title'] or "",
    feature['price'] or "",
    feature['availability'] or "",
    feature['description'] or "")])

print("Данные введены успешно.")


result = client.execute("SELECT * FROM db_books.books")
print("Вставленная запись:", result[900])

