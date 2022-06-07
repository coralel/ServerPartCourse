from flask import Flask, redirect, render_template
from flask import url_for
from flask import render_template
from datetime import timedelta
from flask import request, session, jsonify
app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

app = Flask(__name__)


@app.route('/contactUs')
def goToContacUs():
    return render_template('ContactUs.html')

@app.route('/')
def redirectHomePage():
    return redirect(url_for('goToHomePage'))

@app.route('/homePage')
def goToHomePage():
    return render_template('HomePage.html')

if __name__ == '__main__':
    app.run(debug=True)
