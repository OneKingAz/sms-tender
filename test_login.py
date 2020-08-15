from bottle import Bottle,route, request, static_file, run, get, post, abort
application  = Bottle()

import mysql.connector

mydb = mysql.connector.connect(
  host="*.126.167.134",
  user="*login",
  password="W1ww6y2c",
  database="user8745*"
)
mycursor = mydb.cursor()

###Функция для проверки логина и пароля! 
def check_password(username,password):
    sql = ('SELECT password FROM users_login WHERE login = %s')
    mycursor.execute(sql,username)
    myresult = mycursor.fetchone()
    user_account_password = (myresult[0])
    if user_account_password != password:
        return False
    elif user_account_password == password:
        return True

### Страничка авторизация!!
@get( '/' )
def login():
    return '''
        <form action="/login" method="post">
        Логин: <input name="username" type="text" />
        Пароль: <input name="password" type="password" />
        <input value="Войти" type="submit" />
        </form>    
        <input type="button" value="Проверить ИНН в черном списке!" onClick='location.href="http://localhost:8080/check_inn"'>
    '''
### Страничка для авторизации при проверки ИНН
@get( '/check_inn' )
def return_inn():
    return '''
        <form action="/check_inn" method="post">
        Логин: <input name="username" type="text" />
        Пароль: <input name="password" type="password" />
        ИНН: <input name="inn" type="text" />
        <input value="Проверить" type="submit" />
        </form>    
        
    '''
### POST- запрос с встроенной функцией для проверки ИНН 
@post( '/check_inn' )
def check_inn():
    username = request.forms.username
    password = request.forms.password
    inn = request.forms.inn
    login = tuple([username])
    if check_password(login,password) == True:
        sql = "SELECT * FROM blacklist WHERE inn = %s"
        inn = (inn + ",")
        print(inn)
        mycursor.execute(sql, inn)
        myresult = mycursor.fetchall()
        info = []
        for x in myresult:
            info.append[x]
        print(type(inn))
        print(val)
        
        return info
    elif check_password(login,password) == False:
        return "<p>Вы ввели неправильно логин или пароль!<p>"



@post( '/login' )
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    login = tuple([username])
    if check_password(login,password) == True:
        return yes()
    elif check_password(login,password) == False:
        return "<p>Error!<p>"


def yes():
    return '''
        <form action="/blacklist" method="post">
        <meta charset="utf-8" />
        Ф.И.О: <input name="personname" type="text" />
        Серия и номер паспорта: <input name="passport_id" type="text" />
        ИНН: <input name="inn" type="text" />
        Дата рождения: <input name="person_date" type="date" />
        Дата поподания в черный список: <input name="black_date" type="date" />
        Дата выхода из черного списка : <input name="end_black_date" type="date" />
        <select name="org_name" id="cars">
        <option value="SEZAM">SEZAM</option>
        <option value="Murabaha">Murabaha</option>
        <option value="Zalk">Zalk</option>
        <option value="Qiew">Qiew</option>
        </select>
        Причина поподания в черный список: <input name="coment" type="text" />
        Купленный товар: <input name="tovar" type="text" />
        Сумма долга: <input name="dolg" type="text" />
        <input value="Записать" type="submit" />
        </form>
    '''


@get('/login')
def restricted():
    abort(401, "Пройдите авторизацию!")

@post( '/blacklist' )
def insert():
    personname = request.forms.personname
    passport_id = request.forms.passport_id
    inn = request.forms.inn
    person_date = request.forms.person_date
    black_date = request.forms.black_date
    end_black_date = request.forms.end_black_date
    org_name = request.forms.org_name
    coment = request.forms.coment
    tovar = request.forms.tovar
    dolg = request.forms.dolg
    sql = "INSERT INTO blacklist (personname, passport_id, inn, person_date, black_date, org_name, coment, end_black_date, tovar, dolg ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,  %s)"
    personname.encode("utf-8")
    val = (personname, passport_id, inn, person_date, black_date, org_name, coment,end_black_date, tovar, dolg)
    mycursor.execute(sql, val)
    mydb.commit()
    return ("<p>Данные успешно записаны!<p>")


    
    
run(host='localhost', port=8080, debug=True)
