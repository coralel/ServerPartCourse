# ----------------------------------- import -----------------------------------
from flask import Flask, redirect, render_template, url_for
from datetime import timedelta
from flask import request, session, jsonify


# --------------------------- Create a Flask instance ---------------------------
app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)

# -------------------------- Create a route decorator --------------------------


@app.route('/')
def redirect_homepage():
    return redirect(url_for('go_to_home_page'))


@app.route('/contact_us')
def go_to_contact_us():
    return render_template('ContactUs.html')


@app.route('/home_page')
def go_to_home_page():
    return render_template('HomePage.html')


@app.route('/My_info')
def MyInfo():
    My_info = {'name': 'Coral', 'second_name': 'Elimelech', 'nickname': 'Cori'}
    hobbies = ('Painting', 'Macrame', 'Dance', 'Reality TV', 'Swimming')
    musics = ("We're Good-Dua Lipa", 'Shape Of My Heart-Sting', "You're Beautiful-James Blunt", "You-MARBL")
    return render_template('assignment3_1.html',
                           My_info=My_info,
                           hobbies=hobbies,
                           musics=musics)


@app.route('/searchForms', methods=['GET', 'POST'])
def go_to_assignment3_2():
    # Get Case
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name in user_dict:
                return render_template('assignment3_2.html',
                                       user_username=user_name,
                                       user_lastname=user_dict[user_name][0],
                                       user_age=user_dict[user_name][1],
                                       user_email=user_dict[user_name][2],
                                       nickname=user_dict[user_name][3])
            if len(user_name) == 0:
                return render_template('assignment3_2.html',
                                       user_dict=user_dict)
            else:
                return render_template('assignment3_2.html', message='User is not found')
    # Post Case
    if request.method == 'POST':
        reg_username = request.form['username']
        reg_lastname = request.form['user_lastname']
        reg_email = request.form['email']
        reg_age = request.form['age']
        reg_nickname = request.form['nickname']
        session['username'] = reg_username
        session['user_lastname'] = reg_lastname
        session['email'] = reg_email
        session['age'] = reg_age
        session['nickname'] = reg_nickname
        session['Registered'] = True
        return render_template('assignment3_2.html')

    return render_template('assignment3_2.html')


@app.route('/session')
def session_func():
    # print(session['CHECK'])
    return jsonify(dict(session))


user_dict = {
    'Coral': ['Cori@gmail.com', 'Elimelech', '25', 'Cori'],
    'Maya': ['Mimi@gmail.com', 'Dagan', '26', 'Mimi'],
    'Ninety': ['Nina@gmail.com', 'Taleb', '27', 'Nina'],
    'Ran': ['Rani@gmail.com', 'Danker', '28', 'Ranran'],
    'Erat': ['Efi@gmail.com', 'Bondavalli', '29', 'Efi'],
    'Roy': ['roro@gmail.com', 'tom', '30', 'Roychu'],
    'Michal': ['michi@gmail.com', 'baba', '31', 'Mimi']
}


@app.route('/log_out')
def logout():
    session['Registered'] = False
    session.clear()
    return redirect(url_for('go_to_assignment3_2'))


if __name__ == '__main__':
    app.run(debug=True)

