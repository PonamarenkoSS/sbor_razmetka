import pandas as pd 
from clickhouse_driver import Client
from datetime import datetime

client = Client('localhost')

data = client.execute('SELECT * FROM db_books.books')
df = pd.DataFrame(data, columns=['id', 'title', 'price', 'availability', 'description']).sort_values(by='id')
print(df.head())
print()

availability_20 = client.execute("SELECT * FROM db_books.books WHERE availability = 20") 
df_availability_20 = pd.DataFrame(availability_20, columns=df.columns).sort_values(by='id')
print(df_availability_20)
print()

price_low_50 = client.execute("SELECT * FROM db_books.books WHERE price < 50")
df_price_low_50 = pd.DataFrame(price_low_50, columns=df.columns).sort_values(by='id')
print(df_price_low_50.head())
print()

availability_count = client.execute("SELECT availability, COUNT(*) as count FROM db_books.books GROUP BY availability ORDER BY availability DESC") 
df_availability_count = pd.DataFrame(availability_count, columns=['availability', 'count'])
print(df_availability_count)
print()

price_avg = client.execute("SELECT ROUND(AVG(price), 2) as price_avg FROM db_books.books") 
print(f'Средняя стоимость книги - {price_avg[0][0]}')