# -*- coding: utf-8 -*-
from flask import Flask, flash, render_template, request, jsonify
from HeadHunterInteraction import HeadHunterInteraction
from repoze.lru import lru_cache
from models import HH, session
app = Flask(__name__)
app.secret_key = 'some_secret'
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
    if request.method == 'POST':
        if "write" in request.form:
            # при нажатии "записать" записываем в БД
            vacancy = request.form['vacancy']
            city = request.form['city']
            hh = HeadHunterInteraction()
            city_id = hh.get_id(nameCity=city)
            skills = hh.get_skills(vacancy, city_id)
            salary = hh.get_salary(vacancy, city_id)
            query = HH(vacancy=vacancy, city=city, salary=salary, skills=skills)
            session.add(query)
            session.commit()
            flash(insert_ok_msg)

        if "writenew" in request.form:
            # при нажатии "записать" записываем в БД введенную вручную вакансию
            vacancy = request.form['vacancy']
            city = request.form['city']
            salary = request.form['salary']
            skills = request.form['skills']
            query = HH(vacancy=vacancy, city=city, salary=salary, skills=skills)
            session.add(query)
            session.commit()
            flash(insert_ok_msg)

        if "search" in request.form:
            #поиск в БД всех вакансий по указанному городу
            search = request.form['search']
            result = session.query(HH).filter(HH.city.like(search))
            if session.query(result.exists()).scalar():
                for res in result:
                    flash(res)
            else:
                flash("Not found")

        if "watch" in request.form:
            records = session.query(HH)
            if session.query(records.exists()).scalar():
                for rec in records:
                    flash(rec)
            else:
                flash("No records in DB")

        if "delete" in request.form:
            session.query(HH).delete()
            session.commit()
            flash("Records deleted")

    session.close()
    return render_template('/service.html')

if __name__ == "__main__":
    app.run(debug = True)