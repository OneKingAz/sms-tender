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



@route('/')
def server_static():
    return ("<p>Hello Word<p")
    ##return static_file('index.html' , root="C:\\GitHub\\sms-tender\\templates")
    

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='C:\\GitHub\\sms-tender\\static')

@get('/register')
def reg():
    return static_file('register.html' , root="C:\\GitHub\\sms-tender\\templates")
    # return '''
    #     <form action="/register" method="post">
    #         Логин: <input name="new_username" type="text" />
    #         Пароль: <input name="password" type="password" />
    #         Потверждение пароля: <input name="password_correct" type="password" />
    #         <p>Введите пожалуйста номер телефона в формате +996(555)123456<p>
    #         Номер телефона: <input name="phone_number" type="text" />
    #         <input value="Вход в систему" type="submit" />
    #         '''

@post('/register') 
def reg_account():
    new_username = request.forms.get('new_username')
    password_correct = request.forms.get('password_correct')
    password = request.forms.get('password')
    phone_number = request.forms.get('phone_number')
<<<<<<< HEAD
=======
    print(new_username,password_correct,password,phone_number)
    
    
>>>>>>> 165a032f01e67338451443aa3261b5d240e63f9d
    login = tuple([new_username])
    phone_number_user = tuple([phone_number])
    password_tuple = tuple([password])
    if password != password_correct:
        return "<p>Пароли различаються<p>"
    elif len(password) < 8:
        return ("<p>Пароль должение быть не меньше 8 символов<p>")
    elif check_login2(login) == 1:
        return ("<p>Введенный логин уже существует!<p>")
    elif check_number(phone_number_user):
        return ("<p>Введенный вами номер уже зарегистрирован<p>")
    #Проверяем логин, на наличие существования!
    sql = "INSERT INTO users_login (login, password, phone_number) VALUES (%s, %s, %s)"
    val = (new_username,password,phone_number)
    mycursor.execute(sql, val)
    mydb.commit()
    return "Поздравляем вы успешно, зарегистрировались в систем, ваши данные {},{},{}".format(new_username,password,phone_number)

def check_login2(username):
    sql_login = ("SELECT EXISTS(SELECT login FROM users_login WHERE login = %s)")
    mycursor.execute(sql_login,username)
    myresult = mycursor.fetchone()
    return myresult[0]
def check_number(phone_number):
    sql_login = ("SELECT EXISTS(SELECT phone_number FROM users_login WHERE phone_number = %s)")
    mycursor.execute(sql_login,phone_number)
    myresult = mycursor.fetchone()
    return myresult[0]

@get('/login') # or @route('/login')
def login():
    return static_file('login.html' , root="C:\\GitHub\\sms-tender\\templates")
    # return '''
    #     <form action="/login" method="post">
    #         Логин: <input name="username" type="text" />
    #         Пароль: <input name="password" type="password" />
    #         <input value="Вход в систему" type="submit" />
    #     </form>
    # '''
@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    login = tuple([username])
    if check_password(login,password) == True:
        resp = static_file('hello.html' , root="C:\\GitHub\\sms-tender\\templates")
        resp.set_cookie("mycookie","lolo")
        return resp
    elif check_password(login,password) == False:
        return "<p>Вы ввели неправильно логин или пароль!<p>"
def check_password(username,password):
    sql = ('SELECT password FROM users_login WHERE login = %s')
    mycursor.execute(sql,username)
    myresult = mycursor.fetchone()
    user_account_password = (myresult[0])
    if user_account_password != password:
        return False
    elif user_account_password == password:
        return True

run(host='localhost', port=8080, debug=True, reloader=True)