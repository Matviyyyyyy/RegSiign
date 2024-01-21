from flask import Flask, render_template, request, flash, redirect
from SQLAgent import SQLAgent
from SQLAgent import*

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registr.html')

@app.route('/register', methods=['POST'])
def register():

    #отримую значення інпутів
    name_user = request.form.get['name_user_id']
    password_user = request.form.get['password_user_id']
    img_url = request.form.get['img_url_id']

    #додаю значення до sql
    sql_agent = SQLAgent("logo-cars-table.db")
    sql_agent.add_user(name_user, password_user, img_url)

@app.route('/sign', methods=['GET'])
def sign_in():
    #отримую значення інпутів
    name_user_sign = request.form['name_user_sign_id']
    password_user_sign = request.form['password_user_sign_id']

    sql_agent = SQLAgent("logo-cars-table.db")
    user = sql_agent.get_correct_user(name_user_sign, password_user_sign)
    if user:
        return render_template("sign_in_page.html")
    else:
        return redirect('/uncorrect')
@app.route('/uncorrect')
def uncorrect_page():
    return render_template('uncorrect.html')







if __name__ == '__main__':
    app.run(debug=True)

"""
vanv/Scripts\activate
python app.py
"""
