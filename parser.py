# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests, csv
import re

URL = 'https://irecommend.ru/content/mobilnyi-telefon-apple-iphone-14-pro'
URL_ = 'https://www.citilink.ru/product/smartfon-apple-iphone-14-a2881-128gb-goluboi-3g-4g-6-1-iphone-ios-16-8-1859460/otzyvy/'
page = requests.get(URL)
page_ = requests.get(URL_)
if page.status_code and page_.status_code == 200:
    soup = BeautifulSoup(page.content, 'html5lib')
    soup_ = BeautifulSoup(page_.content, 'html5lib')
    with open("parse.csv", mode="w") as w_file:
        file_writer = csv.writer(w_file, delimiter="|", lineterminator="\r")
        file_writer.writerow(["Имя автора отзыва", "Отзыв", "Дата"])
        for review in soup.find_all('li', class_="item"):
            text = review.find('div', class_='reviewTitle').get_text().encode('utf-8')
            name = review.find('div', class_='authorName').get_text().encode('utf-8')
            date = review.find('div', class_='created').get_text()
            file_writer.writerow([name, text, date])

else:
    print('Error: ', page.status_code, page_.status_code)

