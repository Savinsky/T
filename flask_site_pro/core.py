# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, jsonify
import requests, sqlite3 as lite, sys
from HeadHunterInteraction import HeadHunterInteraction
from repoze.lru import lru_cache

URL = 'https://api.hh.ru/vacancies'
connect = None
app = Flask(__name__)
app.secret_key = 'some_secret'
insert = "INSERT INTO HH (vacancy, city, salary, skills) VALUES (?,?,?,?)"

insert_ok_msg = "Record successfully added!"
@app.route("/")
@app.route("/main")
#@lru_cache(maxsize=100)
def main():
    return render_template('main.html')

@app.route("/contacts")
#@lru_cache(maxsize=100)
def contacts():
    return render_template('/contacts.html')

@app.route("/service", methods = ['GET', 'POST'])
#@lru_cache(maxsize=100)
def service():
    # Создаем таблицу, если не создана
    try:
        connect = lite.connect('database.db')
        cur = connect.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS HH (id INTEGER PRIMARY KEY AUTOINCREMENT, vacancy TEXT, "
                    "city TEXT, salary REAL, skills TEXT)")
    except lite.Error as e:
        flash("Error {}:".format(e.args[0]))
        sys.exit(1)
    if request.method == 'POST':
        try:
            with lite.connect("database.db") as con:
                if "write" in request.form:
                    # при нажатии "записать" записываем в БД
                    vacancy = request.form['vacancy']
                    city = request.form['city']
                    hh = HeadHunterInteraction()
                    city_id = hh.get_id(nameCity=city)
                    skills = hh.get_skills(vacancy, city_id)
                    salary = hh.get_salary(vacancy, city_id)
                    cur = con.cursor()
                    cur.execute(insert, (vacancy, city, salary, skills))
                    con.commit()
                    flash(insert_ok_msg)

                if "writenew" in request.form:
                    # при нажатии "записать" записываем в БД введенную вручную вакансию
                    vacancy = request.form['vacancy']
                    city = request.form['city']
                    salary = request.form['salary']
                    skills = request.form['skills']
                    cur = con.cursor()
                    cur.execute(insert, (vacancy, city, salary, skills))
                    con.commit()
                    flash(insert_ok_msg)

                if "search" in request.form:
                    #поиск в БД всех вакансий по указанному городу
                    search = request.form['search']
                    cur = con.cursor()
                    cur.execute("SELECT * FROM HH WHERE city LIKE '{}'".format(search))
                    result = cur.fetchall()
                    flash(result)

                if "watch" in request.form:
                    cur = con.cursor()
                    cur.execute("SELECT *from HH")
                    records = cur.fetchall()
                    flash(records)

        except:
           con.rollback()
           flash("Error in operation!")


    if connect:
        connect.close()
    return render_template('/service.html')

if __name__ == "__main__":
    app.run(debug = True)