# -*- coding: utf-8 -*-
import requests
URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python', 'area': '1', 'period': '30', 'only_with_salary': 'true', 'per_page': '100'}
response = requests.get(URL, params=params).json()
salar_from = [] #Зарплата от...
salar_to = []  #Зарплата до ...
for item in response['items']:
    if item['salary'] is not None and item['salary']['currency'] == 'RUR':
        if item['salary']['from'] is not None:
            salar_from.append(item['salary']['from'])
        elif item['salary']['to'] is not None:
            salar_to.append(item['salary']['to'])

avarage_salar_from = sum(salar_from) / len(salar_from) # В среднем от...
avarage_salar_to = sum(salar_to) / len(salar_to) # В среднем до...


print('Найдено вакансий на hh.ru с указанным уровнем дохода в рублях по запросу Python в Москве : {}'.format(response['found']))
print('Со средней заплатой от {} руб до {} руб'.format(avarage_salar_from, avarage_salar_to))