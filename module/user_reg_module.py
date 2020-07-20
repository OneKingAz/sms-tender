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

@get('/')
def hello():
    return (""" <!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Login</title>
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css">
    </head>
    <body>
        <div class="login">
            <h1>Login</h1>
            <div class="links">
                <a href="login" class="active">Login</a>
                <a href="register">Register</a>
            </div>
            <form action="login" method="post">
                <label for="username">
                    <i class="fas fa-user"></i>
                </label>
                <input type="text" name="username" placeholder="Username" id="username" required>
                <label for="password">
                    <i class="fas fa-lock"></i>
                </label>
                <input type="password" name="password" placeholder="Password" id="password" required>
                <div class="msg">{{ msg }}</div>
                <input type="submit" value="Login">
            </form>
        </div>
    </body>
    <style>
    * {
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "segoe ui", roboto, oxygen, ubuntu, cantarell, "fira sans", "droid sans", "helvetica neue", Arial, sans-serif;
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
body {
    background-color: #435165;
    margin: 0;
}
.login, .register {
    width: 400px;
    background-color: #ffffff;
    box-shadow: 0 0 9px 0 rgba(0, 0, 0, 0.3);
    margin: 100px auto;
}
.login h1, .register h1 {
    text-align: center;
    color: #5b6574;
    font-size: 24px;
    padding: 20px 0 20px 0;
    border-bottom: 1px solid #dee0e4;
}
.login .links, .register .links {
    display: flex;
    padding: 0 15px;
}
.login .links a, .register .links a {
    color: #adb2ba;
    text-decoration: none;
    display: inline-flex;
    padding: 0 10px 10px 10px;
    font-weight: bold;
}
.login .links a:hover, .register .links a:hover {
    color: #9da3ac;
}
.login .links a.active, .register .links a.active {
    border-bottom: 3px solid #3274d6;
    color: #3274d6;
}
.login form, .register form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-top: 20px;
}
.login form label, .register form label {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    background-color: #3274d6;
    color: #ffffff;
}
.login form input[type="password"], .login form input[type="text"], .login form input[type="email"], .register form input[type="password"], .register form input[type="text"], .register form input[type="email"] {
    width: 310px;
    height: 50px;
    border: 1px solid #dee0e4;
    margin-bottom: 20px;
    padding: 0 15px;
}
.login form input[type="submit"], .register form input[type="submit"] {
    width: 100%;
    padding: 15px;
    margin-top: 20px;
    background-color: #3274d6;
    border: 0;
    cursor: pointer;
    font-weight: bold;
    color: #ffffff;
    transition: background-color 0.2s;
}
.login form input[type="submit"]:hover, .register form input[type="submit"]:hover {
    background-color: #2868c7;
    transition: background-color 0.2s;
}
.navtop {
    background-color: #2f3947;
    height: 60px;
    width: 100%;
    border: 0;
}
.navtop div {
    display: flex;
    margin: 0 auto;
    width: 1000px;
    height: 100%;
}
.navtop div h1, .navtop div a {
    display: inline-flex;
    align-items: center;
}
.navtop div h1 {
    flex: 1;
    font-size: 24px;
    padding: 0;
   margin: 0;
    color: #eaebed;
    font-weight: normal;
}
.navtop div a {
    padding: 0 20px;
    text-decoration: none;
    color: #c1c4c8;
    font-weight: bold;
}
.navtop div a i {
    padding: 2px 8px 0 0;
}
.navtop div a:hover {
    color: #eaebed;
}
body.loggedin {
    background-color: #f3f4f7;
}
.content {
    width: 1000px;
    margin: 0 auto;
}
.content h2 {
    margin: 0;
    padding: 25px 0;
    font-size: 22px;
    border-bottom: 1px solid #e0e0e3;
    color: #4a536e;
}
.content > p, .content > div {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
    margin: 25px 0;
    padding: 25px;
  background-color: #fff;
}
.content > p table td, .content > div table td {
  padding: 5px;
}
.content > p table td:first-child, .content > div table td:first-child {
  font-weight: bold;
  color: #4a536e;
  padding-right: 15px;
}
.content > div p {
  padding: 5px;
  margin: 0 0 10px 0;
}
    </style>
</html>""") 
    
@get('/register')
def reg():
    return '''<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Регистрация</title>
        <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css">
    </head>
    <body>
        <div class="register">
            <h1>Регистрация</h1>
            <div class="links">
                <a href="login">Войти</a>
                <a href="register" class="active">Введите свои данные</a>
            </div>
            <form action="register" method="post" autocomplete="off">
                <label for="Придумайте логин">
                    <i class="fas fa-user"></i>
                </label>
                <input name="new_username" type="text" />
                <label for="Придумайте пароль">
                    <i class="fas fa-lock"></i>
                </label>
                 <input name="password" type="password" />
                <label for="Потверждение пароля">
                    <i class="fas fa-lock"></i>
                </label>
                <input name="password_correct" type="password" />
                <label for="Номер телефона">
                    <i class="fas fa-envelope"></i>
                </label>
                <input name="phone_number" type="text" />
                
                <input type="submit" value="Зарегистрироваться">
            </form>
        </div>
        <style>
    * {
    box-sizing: border-box;
    font-family: -apple-system, BlinkMacSystemFont, "segoe ui", roboto, oxygen, ubuntu, cantarell, "fira sans", "droid sans", "helvetica neue", Arial, sans-serif;
    font-size: 16px;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}
body {
    background-color: #435165;
    margin: 0;
}
.login, .register {
    width: 400px;
    background-color: #ffffff;
    box-shadow: 0 0 9px 0 rgba(0, 0, 0, 0.3);
    margin: 100px auto;
}
.login h1, .register h1 {
    text-align: center;
    color: #5b6574;
    font-size: 24px;
    padding: 20px 0 20px 0;
    border-bottom: 1px solid #dee0e4;
}
.login .links, .register .links {
    display: flex;
    padding: 0 15px;
}
.login .links a, .register .links a {
    color: #adb2ba;
    text-decoration: none;
    display: inline-flex;
    padding: 0 10px 10px 10px;
    font-weight: bold;
}
.login .links a:hover, .register .links a:hover {
    color: #9da3ac;
}
.login .links a.active, .register .links a.active {
    border-bottom: 3px solid #3274d6;
    color: #3274d6;
}
.login form, .register form {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    padding-top: 20px;
}
.login form label, .register form label {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    background-color: #3274d6;
    color: #ffffff;
}
.login form input[type="password"], .login form input[type="text"], .login form input[type="email"], .register form input[type="password"], .register form input[type="text"], .register form input[type="email"] {
    width: 310px;
    height: 50px;
    border: 1px solid #dee0e4;
    margin-bottom: 20px;
    padding: 0 15px;
}
.login form input[type="submit"], .register form input[type="submit"] {
    width: 100%;
    padding: 15px;
    margin-top: 20px;
    background-color: #3274d6;
    border: 0;
    cursor: pointer;
    font-weight: bold;
    color: #ffffff;
    transition: background-color 0.2s;
}
.login form input[type="submit"]:hover, .register form input[type="submit"]:hover {
    background-color: #2868c7;
    transition: background-color 0.2s;
}
.navtop {
    background-color: #2f3947;
    height: 60px;
    width: 100%;
    border: 0;
}
.navtop div {
    display: flex;
    margin: 0 auto;
    width: 1000px;
    height: 100%;
}
.navtop div h1, .navtop div a {
    display: inline-flex;
    align-items: center;
}
.navtop div h1 {
    flex: 1;
    font-size: 24px;
    padding: 0;
   margin: 0;
    color: #eaebed;
    font-weight: normal;
}
.navtop div a {
    padding: 0 20px;
    text-decoration: none;
    color: #c1c4c8;
    font-weight: bold;
}
.navtop div a i {
    padding: 2px 8px 0 0;
}
.navtop div a:hover {
    color: #eaebed;
}
body.loggedin {
    background-color: #f3f4f7;
}
.content {
    width: 1000px;
    margin: 0 auto;
}
.content h2 {
    margin: 0;
    padding: 25px 0;
    font-size: 22px;
    border-bottom: 1px solid #e0e0e3;
    color: #4a536e;
}
.content > p, .content > div {
    box-shadow: 0 0 5px 0 rgba(0, 0, 0, 0.1);
    margin: 25px 0;
    padding: 25px;
  background-color: #fff;
}
.content > p table td, .content > div table td {
  padding: 5px;
}
.content > p table td:first-child, .content > div table td:first-child {
  font-weight: bold;
  color: #4a536e;
  padding-right: 15px;
}
.content > div p {
  padding: 5px;
  margin: 0 0 10px 0;
}
    </style>
    </body>
</html>
    '''

@post('/register') 
def reg_account():
    new_username = request.forms.get('new_username')
    password_correct = request.forms.get('password_correct')
    password = request.forms.get('password')
    phone_number = request.forms.get('phone_number')
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
    login = tuple([username])
    if check_password(login,password) == True:
        return "<p>Добро пожаловать!<p>"
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

run(host='localhost', port=8080, debug=True)