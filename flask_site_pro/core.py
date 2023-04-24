# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import requests
from new import HeadHunterInteraction
URL = 'https://api.hh.ru/vacancies'

app = Flask(__name__)
@app.route("/")
@app.route("/main")
def main():

    return render_template('main.html')

@app.route("/contacts")
def contacts():
    #data = {}
    return render_template('/contacts.html') #, data=data)

@app.route("/service", methods = ['GET', 'POST'])
def service():
    if request.method == 'POST':
        hh = HeadHunterInteraction()

        vacancy = request.form['vacancy']

        city = request.form['city']
        city_id = hh.get_id(nameCity=city)
        get_skills = hh.get_skills(vacancy, city_id)
        get_salary = hh.get_salary(vacancy, city_id)
        data = {
        'skills': get_skills,
        'vacancy': vacancy,
        'city': city,
        'salary': get_salary}

        #vacancy = request.form.get('vacancy')
        #city = request.form.get('city')
        return render_template('/service.html', data=data)
    else:
        return render_template('/service.html', data=None)
"""
def f_snippet(page, search):
    '''Навыки на одной странице'''
    snippet = [] # здесь сохраняю навыки от соискателя
    params = {'text': '{}'.format(search), 'page': page}
    vacancies = requests.get(URL, params=params).json()
    for item in vacancies['items']:
        if item['snippet']['requirement']:# &['responsibility']:
            snippet.append(item['snippet']['requirement']) #&['responsibility'])
    return snippet

def get_skills_and_salary(vacancy):
    params = {'text': '{}'.format(vacancy), 'area': 1, 'period': '30', 'only_with_salary': 'true', 'per_page': '100'}
    response = requests.get(URL, params=params)
    pages = response.json()['pages']
    search = vacancy

    req = []  # список слов
    for page in range(pages):
        for char in f_snippet(page, search):
            req.extend(char.split())
    sym = [',', '.', ';', ':', '<highlighttext>', '</highlighttext>', '/', ')', '(', 'e.g.', '-']
    # первичная грубая очистка текста
    for i in range(len(req)):
        for s in sym:
            if s in req[i].lower():
                req[i] = req[i].replace(s, '')

    req_resault = [item.lower() for item in req if item]
    my_dict = {}
    for k in req_resault:
        my_dict[k] = req_resault.count(k)

    skills = list(my_dict.items())
    skills.sort(key=lambda x: x[1], reverse=True)
    #return skills


    salar_from = []
    salar_to = []
    response = requests.get(URL, params=params).json()
    for item in response['items']:
        if item['salary'] is not None and item['salary']['currency'] == 'RUR':
            if item['salary']['from'] is not None:
                salar_from.append(item['salary']['from'])
            elif item['salary']['to'] is not None:
                salar_to.append(item['salary']['to'])

    quantity = response['found']
    avarage_salar_from = sum(salar_from) / len(salar_from)
    avarage_salar_to = sum(salar_to) / len(salar_to)

    return skills[10], quantity, avarage_salar_to, avarage_salar_from
"""
if __name__ == "__main__":
    app.run(debug = True)