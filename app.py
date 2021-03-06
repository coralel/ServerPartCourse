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

# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------ASSIGNMENT 3-----------ASSIGNMENT 3-----------ASSIGNMENT 3-----------ASSIGNMENT 3-----------ASSIGNMENT 3----------------------
# -----------------------------------------------------------------------------------------------------------------------------------------


@app.route('/')
def redirect_homepage():
    return redirect(url_for('go_to_home_page'))


@app.route('/contact_us')
def go_to_contact_us():
    Clear_sessions()
    return render_template('ContactUs.html')


@app.route('/home_page')
def go_to_home_page():
    Clear_sessions()
    return render_template('HomePage.html')


@app.route('/My_info')
def MyInfo():
    Clear_sessions()
    My_info = {'name': 'Coral', 'second_name': 'Elimelech', 'nickname': 'Cori'}
    hobbies = ('Painting', 'Macrame', 'Dance', 'Reality TV', 'Swimming')
    musics = ("We're Good-Dua Lipa", 'Shape Of My Heart-Sting', "You're Beautiful-James Blunt", "You-MARBL")
    return render_template('assignment3_1.html',
                           My_info=My_info,
                           hobbies=hobbies,
                           musics=musics,
                           message1='My hobbies are yours too?')


@app.route('/terminalX')
def terminalX():
    return redirect("https://www.terminalx.com//")


@app.route('/searchForms', methods=['GET', 'POST'])
def go_to_assignment3_2():
    Clear_sessions()
    # Get Case
    if request.method == 'GET':
        if 'user_name' in request.args:
            user_name = request.args['user_name']
            if user_name in user_dict:
                return render_template('assignment3_2.html',
                                       user_username=user_name,
                                       user_lastname=user_dict[user_name][1],
                                       user_age=user_dict[user_name][2],
                                       user_email=user_dict[user_name][0],
                                       nickname=user_dict[user_name][3])
            if len(user_name) == 0:
                return render_template('assignment3_2.html',
                                       user_dict=user_dict)
            else:
                return render_template('assignment3_2.html', message='Who it is?')
    # Post Case
    if request.method == 'POST':
        reg_username = request.form['username']
        if reg_username in user_dict:
            reg_nickname = user_dict[reg_username][3]
            session['nickname'] = reg_nickname
            session['Registered'] = True
            return render_template('assignment3_2.html', message2='I already know you!')
        else:
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
            user_dict[reg_username] = (reg_email, reg_lastname, reg_age, reg_nickname)
            return render_template('assignment3_2.html', message2='Welcome my new friend! registration was successful!')

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


# ----------------------------------------------------------------------------------------------------------------------------------------
# -----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4----------------------
# ----------------------------------------------------------------------------------------------------------------------------------------


# ------users Blueprint-------
from users.assignment4 import assignment_4
app.register_blueprint(assignment_4)


# ------------------------------- CLEAR SESSIONS FROM ASS 4 -----------------------------------
def Clear_sessions():
    session['INSERT'] = False
    session['DELETE'] = False
    session['UPDATE'] = False
    session['ERROR'] = False


if __name__ == '__main__':
    app.run(debug=True)
