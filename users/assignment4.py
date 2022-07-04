# ----------------------------------- import -----------------------------------
import json
from flask import Blueprint, render_template
from flask import Flask, redirect, url_for
from flask import request, session, jsonify, json
import mysql.connector
import requests
from settings import DB
from app import app

assignment_4 = Blueprint('users', __name__,
                         static_folder='static',
                         static_url_path='/users',
                         template_folder='templates')


# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4-----------ASSIGNMENT 4----------------------
# -----------------------------------------------------------------------------------------------------------------------------------------


# -------------------------- Database Connection Command --------------------------

def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(**DB)
    #connection = mysql.connector.connect(host='localhost',
     #                                    user='root',
      #                                   passwd='root',
       #                                  database='myflaskappdb')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        # Commit use for INSERT, UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        # Fetch use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


# ------------------------------- CLEAR SESSIONS-----------------------------------
def Clear_sessions():
    session['INSERT'] = False
    session['DELETE'] = False
    session['UPDATE'] = False
    session['ERROR'] = False


# ----------------------------------- SELECT --------------------------------------
@assignment_4.route('/select_users')
def select_users():
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    return render_template('assignment_4.html', users=users_list)


# ----------------------------------- INSERT --------------------------------------
@assignment_4.route('/insert_user', methods=['POST'])
def insert_user():
    Clear_sessions()
    ID = request.form['userID']
    username = request.form['username']
    email = request.form['email']
    lastname = request.form['user_lastname']
    age = request.form['age']
    nickname = request.form['nickname']
    session['INSERT'] = True

    isInDB = "select * FROM users WHERE ID='%s';" % ID
    usersList = interact_db(isInDB, query_type='fetch')

    if len(usersList) > 0:
        insert_message_txt = 'There is user with that ID already'
    else:
        query = "INSERT INTO users(ID, name, email, lastName, age, nickname) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            ID, username, email, lastname, age, nickname)
        interact_db(query=query, query_type='commit')
        insert_message_txt = 'The Insertion successfully'
    session['insertMessage'] = insert_message_txt
    return redirect(url_for('users.select_users'))


# ----------------------------------- UPDATE --------------------------------------
@assignment_4.route('/update_user', methods=['POST'])
def update_user():
    Clear_sessions()
    ID = request.form['userID']
    username = request.form['username']
    email = request.form['email']
    lastname = request.form['user_lastname']
    age = request.form['age']
    nickname = request.form['nickname']
    session['UPDATE'] = True
    connection = mysql.connector.connect(**DB)
    #connection = mysql.connector.connect(host='localhost',
                   #                      user='root',
                    #                     passwd='root',
                     #                    database='myflaskappdb')
    isInDB = "select * FROM users WHERE ID='%s';" % ID
    usersList = interact_db(isInDB, query_type='fetch')

    if len(usersList) > 0:
        updateCursor = connection.cursor()
        updateCursor.execute('''
            UPDATE users
            SET name = %s, email = %s, lastname = %s, age = %s, nickname = %s
            WHERE ID = %s
            ''', (username, email, lastname, age, nickname, ID))
        connection.commit()
        insert_message_txt = 'The update successfully'
    else:
        insert_message_txt = 'There is no user with that ID to update'
    session['insertMessage'] = insert_message_txt
    return redirect(url_for('users.select_users'))


# ----------------------------------- DELETE --------------------------------------
@assignment_4.route('/delete_user', methods=['POST'])
def delete_user():
    Clear_sessions()
    session['DELETE'] = True
    ID = request.form['userID']
    table = 'select * from users'
    users_before = interact_db(table, query_type='fetch')
    query = "DELETE FROM users WHERE ID='%s';" % ID
    interact_db(query, query_type='commit')
    table = 'select * from users'
    users_after = interact_db(table, query_type='fetch')
    if len(users_before) > len(users_after):
        insert_message_txt = 'The user is deleted'
    else:
        insert_message_txt = 'There is no user with that ID'
    session['insertMessage'] = insert_message_txt
    return redirect(url_for('users.select_users'))


# ----------------------------------- PART B --------------------------------------
@assignment_4.route('/assignment4/users')
def assignment4_users():
    Clear_sessions()
    query = 'select * from users'
    users_list = interact_db(query, query_type='fetch')
    users_json = json.dumps(users_list)
    return render_template('ass4_users.html', users=users_json)


# -------------------------------------------------------------
def get_User(ID):
    selectedUser = []
    res = requests.get(f'https://reqres.in/api/users/{ID}')
    selectedUser.append(res.json())
    return selectedUser


def save_user_to_session(selectedUser):
    user_to_save = []
    for user in selectedUser:
        selectedUser = {'data': {'avatar': user['data']['avatar']},
                        'email': user['data']['email'],
                        'first_name': user['data']['first_name'], }
        user_to_save.append(selectedUser)
    session['selectedUser'] = user_to_save


@assignment_4.route('/assignment4/outer_source')
def fetch_fe_func():
    Clear_sessions()
    return render_template('ass4_outerSource.html')


@assignment_4.route('/fetch_be')
def fetch_be_func():
    ID = int(request.args['num_id'])
    session['num'] = ID
    selectedUser = get_User(ID)
    save_user_to_session(selectedUser)
    return redirect('/assignment4/outer_source')


# ----------------------------------- PART C --------------------------------------
@assignment_4.route('/assignment4/restapi_users', defaults={'USER_ID': 1})
@assignment_4.route('/assignment4/restapi_users/<int:USER_ID>')
def assignment4_restapi_users(USER_ID):
    Clear_sessions()
    session['ERROR'] = True
    queryName = "select * FROM users WHERE ID='%s';" % USER_ID
    restapi_user = interact_db(queryName, query_type='fetch')
    if len(restapi_user) > 0:
        user = json.dumps(restapi_user)
        session['errorMessage'] = ''
        return render_template('ass4_restapiUsers.html', user=user)
    else:
        errorMessage = 'The user is not exist in our registers'
        session['errorMessage'] = json.dumps(errorMessage)
        return render_template('ass4_restapiUsers.html')
