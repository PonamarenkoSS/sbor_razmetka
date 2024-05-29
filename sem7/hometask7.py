from selenium import webdriver # класс управления браузером
from selenium.webdriver.chrome.options import Options # Настройки
from selenium.webdriver.common.by import By # селекторы
from selenium.webdriver.support.ui import WebDriverWait # класс для ожидания
from selenium.webdriver.support import expected_conditions as EC
import time
import json


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"

url = 'https://rutube.ru/channel/18010012/videos/'

chrome_option = Options()
chrome_option.add_argument(f'{user_agent=}')

driver = webdriver.Chrome(options=chrome_option)
try:
    driver.get(url)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    time.sleep(5)

    while True:
        page_hieght = driver.execute_script("return document.documentElement.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(2)
        page_hieght_new = driver.execute_script("return document.documentElement.scrollHeight")
        if page_hieght_new == page_hieght:
            break
        time.sleep(2)

    value = '//*[@id="root"]/div/div[3]/div/main/div/section/section/div/div/div/article/div/div[1]/a'
    video_titles = driver.find_elements(By.XPATH, value)
    data = []
    for i in range(len(video_titles)):
        video_title = {'title': video_titles[i].text}
        data.append(video_title)

    with open('video_rutube.json', 'w', encoding='U8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


except Exception as er:
    print('error')

finally:
    driver.quit()