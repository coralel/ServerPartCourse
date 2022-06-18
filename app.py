# ----------------------------------- import -----------------------------------
from flask import Flask, redirect, render_template
from flask import url_for
from datetime import timedelta
from flask import request, session, jsonify

# Create a Flask instance
app = Flask(__name__)





app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

app = Flask(__name__)


# https://www.youtube.com/watch?v=4yaG-jFfePc
# @app.route('/contactUs')
# def PageName(pageName):
#    return render_template('PageName.html', name=pageName)

# -------------------------- Create a route decorator --------------------------
@app.route('/ContactUs')
def goToContactUs():
    return render_template('ContactUs.html')


@app.route('/HomePage')
def goToHomePage():
    return render_template('HomePage.html')


if __name__ == '__main__':
    app.run(debug=True)
