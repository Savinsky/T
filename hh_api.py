# -*- coding: utf-8 -*-
import pprint
import requests

URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python', 'area': 1, 'per_page': 100}
response = requests.get(URL, params=params)
if response.status_code == 200:
    vacancies = response.json()['items']
    skills_dict = {}
    for vacancy in vacancies:
        key_skills = vacancy['key_skills']
        for skill in key_skills:
            if skill['name'] in skills_dict:
                skills_dict[skill['name']] += 1
            else:
                skills_dict[skill['name']] = 1

    sorted_skills = sorted(skills_dict.items(), key=lambda x: x[1], reverse=True)[:10]
    for skill in sorted_skills:
        print(skill[0], skill[1])

else:
    print('Error: ', response.status_code)


