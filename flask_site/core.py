from flask import Flask, render_template, request
import requests

URL = 'https://api.hh.ru/vacancies'
params = {'text': 'Python', 'area': '1', 'period': '30', 'only_with_salary': 'true', 'per_page': '100'}
response = requests.get(URL, params=params).json()
salar_from = []
salar_to = []
for item in response['items']:
    if item['salary'] is not None and item['salary']['currency'] == 'RUR':
        if item['salary']['from'] is not None:
            salar_from.append(item['salary']['from'])
        elif item['salary']['to'] is not None:
            salar_to.append(item['salary']['to'])

quantity = response['found']
# quantity =
avarage_salar_from = sum(salar_from) / len(salar_from)
avarage_salar_to = sum(salar_to) / len(salar_to)

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
        data = {
            'quantity': quantity,
            'avarage_salar_from': avarage_salar_from,
            'avarage_salar_to': avarage_salar_to}

        #vacancy = request.form.get('vacancy')
        #city = request.form.get('city')
        return render_template('/service.html', data= data)
    else:
        return render_template('/service.html', data=None)

if __name__ == "__main__":
    app.run(debug = True)