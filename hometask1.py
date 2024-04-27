'''
1. Ознакомиться с некоторые интересными API. 
https://docs.ozon.ru/api/seller/ 
https://developers.google.com/youtube/v3/getting-started 
https://spoonacular.com/food-api
2. Потренируйтесь делать запросы к API. Выберите публичный API, который вас интересует, 
и потренируйтесь делать API-запросы с помощью Postman. Поэкспериментируйте с различными 
типами запросов и попробуйте получить различные типы данных.
'''

import requests
import json

key = '3b886c3112134fda8ca95339660f0ec9'
url = f'https://api.spoonacular.com/recipes/716429/information?apiKey={key}&includeNutrition=true'
url2 = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={key}&ingredients=apples,+flour,+sugar&number=2'

response = requests.get(url)

if response.status_code == 200:
    print('Успешный запрос')
    print(response.text)
else: 
    print('Фиаско')
    print(response.status_code)

response2 = requests.get(url2)

if response2.status_code == 200:
    print('Успешный запрос')
    data = json.loads(response2.text)
    for value in data:
        print(value['title'])
        print()
else: 
    print('Фиаско')
    print(response2.status_code)


'''
3. Сценарий Foursquare
4. Напишите сценарий на языке Python, который предложит пользователю ввести
 интересующую его категорию (например, кофейни, музеи, парки и т.д.).
5. Используйте API Foursquare для поиска заведений в указанной категории.
6. Получите название заведения, его адрес и рейтинг для каждого из них.
7. Скрипт должен вывести название и адрес и рейтинг каждого заведения в консоль.
'''

client_id = "__"
client_secret = "__"

endpoint = "https://api.foursquare.com/v3/places/search"

place = input("Введите заведение: ")
params = {
"client_id": client_id,
"client_secret": client_secret,
"query": place
}

headers = {
"Accept": "application/json",
"Authorization": "fsq3V3AFHzvqod5PVkb9j5ptfec29VfLTGG2XbHrQEGC8bI="
}

response = requests.get(endpoint, params=params, headers=headers)

if response.status_code == 200:
    print("Успешный запрос")
    data = json.loads(response.text)
    venues = data["results"] 
    for venue in venues:
        print("Название:", venue["name"])
        try:
            print("Адрес:", venue["location"]["address"])
        except KeyError:    
            print("Адрес: none",)
        print("Часовой пояс:", venue["timezone"]) 
        print("Страна:", venue["location"]["country"])
        print("\n")
