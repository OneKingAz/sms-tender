from bottle import get, post, request, route, run,static_file
import sys
import os
import mysql.connector
mydb = mysql.connector.connect(
  host="176.126.167.134",
  user="user8745_login",
  password="W1ww6y2c",
  database="user8745_login"
)
mycursor = mydb.cursor()
os.access(r"index.html", os.F_OK)
@route('/')
def hello():
    return static_file("index.html", root='/') 

@get('/reg')
def reg():
    return '''
        <form action="/reg" method="post">
            Логин: <input name="new_username" type="text" />
            Пароль: <input name="password" type="password" />
            Потверждение пароля: <input name="password_correct" type="password" />
            <p>Введите пожалуйста номер телефона в формате +996(555)123456
            Номер телефона: <input name="phone_number" type="text" />
            <input value="Зарегистрироваться" type="submit" />
        </form>
    '''

@post('/reg') 
def reg_account():
    new_username = request.forms.get('new_username')
    password_correct = request.forms.get('password_correct')
    password = request.forms.get('password')
    phone_number = request.forms.get('phone_number')
    if password != password_correct:
        return "<p>Пароли различаються<p>"
    sql = "INSERT INTO users_login (login, password, phone_number) VALUES (%s, %s, %s)"
    val = (new_username, password, phone_number)
    mycursor.execute(sql, val)
    mydb.commit()
    return "Поздравляем вы успешно, зарегистрировались в систем, ваши данные {},{},{}".format(new_username,password,phone_number)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Логин: <input name="username" type="text" />
            Пароль: <input name="password" type="password" />
            <input value="Вход в систему" type="submit" />
        </form>
    '''
    

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    print("Пользователь вводить следующие данные в браузер {}").format(username)
    print(type(username))
    print("Пользователь вводить следующий пароль{}").format(password)
    login = tuple(username)
    print("Фреймворк преобразует его в кортеж {}").format(login)
    print(type(login))
    return (check_login(login,password))
def check_login(username,password):
    sql = "SELECT password FROM users_login WHERE login = %s"
    print("Функция check_login, получает аргумент {}").format(username)
    print(type(username))
    print("Пароль check_login{}").format(password)
    print(type(password))
    
    mycursor.execute(sql,username)
    myresult = mycursor.fetchall()
    sql_password = []
    for x in myresult:
      sql_password.append(x)
    print("Пароль который получил от SQL-сервер{}").format(sql_password)
    print (type(sql_password))
    if sql_password[0] == password:
        return True
    elif sql_password != password:
            return False
    
        
    
        
run(host='localhost', port=8080, debug=True)