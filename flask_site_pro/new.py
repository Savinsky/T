# -*- coding: utf-8 -*-
import requests

class HeadHunterInteraction:
    def __init__(self):
        self.URL = 'https://api.hh.ru'
        self.vacancyURL = '{}/vacancies'.format(self.URL)
        self.country = 'Россия'.decode('utf-8')

    def get_id(self, nameCity):
        # Страна: область/край/республика : Город:
        url_area = '{}/areas'.format(self.URL)
        response = requests.get(url_area).json()   # список [0] из словарей стран
        res = ''
        for dicCountrys in response:
            if dicCountrys['name'] == self.country:
                # словарь областей нужной страны
                idCountry = dicCountrys['id']  # ID нужной страны
                lstRegions = dicCountrys['areas'] # список словарей областей

                for dicRegion in lstRegions:
                    # словарь области с городами

                    #print( dicRegion['name'], nameCity )
                    if dicRegion['name'] == nameCity:
                        idRegion = dicRegion['parent_id']
                        idCity = dicRegion['id']
                        res = (idCountry, idRegion, idCity)
                        break

                    lstCitys = dicRegion['areas']
                    for dicCity in lstCitys:
                        # словарь города
                        if dicCity['name'] == nameCity:
                            # нужный город
                            idRegion = dicCity['parent_id']
                            idCity = dicCity['id']
                            res = (idCountry, idRegion, idCity )
                            break
                    if res:
                        break
                if res:
                    break
            if res:
                break

        if res:
            self.cur_city = [res[2], nameCity]  # Запомнить выбор города

        return res[2]

    def f_snippet(self, page, search):
        snippet = []  # здесь сохраняю навыки от соискателя
        params = {'text': '{}'.format(search), 'page': page}
        vacancies = requests.get(self.vacancyURL, params=params).json()
        for item in vacancies['items']:
            if item['snippet']['requirement']: #|item['snippet']['responsibility']:
                snippet.append(item['snippet']['requirement'])
                #snippet.append(item['snippet']['responsibility'])
        return snippet

    def get_skills(self, vacancy, id_city):
        params = {'text': '{}'.format(vacancy), 'area': '{}'.format(id_city), 'period': '30', 'only_with_salary': 'true', 'per_page': '100'}
        response = requests.get(self.vacancyURL, params=params)
        pages = response.json()['pages']
        search = vacancy

        req = []  # список слов
        for page in range(pages):
            for char in self.f_snippet(page, search):
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
        return skills[:15]

    def get_salary(self, vacancy, id_city):
        params = {'text': '{}'.format(vacancy), 'area': '{}'.format(id_city), 'period': '30', 'only_with_salary': 'true', 'per_page': '100'}
        response = requests.get(self.vacancyURL, params=params).json()
        salar_from = []
        salar_to = []

        for item in response['items']:
            if item['salary'] is not None and item['salary']['currency'] == 'RUR':
                if item['salary']['from'] is not None:
                    salar_from.append(item['salary']['from'])
                elif item['salary']['to'] is not None:
                    salar_to.append(item['salary']['to'])

        #quantity = response['found']
        avarage_salar_from = sum(salar_from) / len(salar_from)
        avarage_salar_to = sum(salar_to) / len(salar_to)

        return avarage_salar_from, avarage_salar_to
