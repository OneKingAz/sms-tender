from bottle import get, post, request, route, run
import mysql.connector
mydb = mysql.connector.connect(
  host="176.126.167.134",
  user="user8745_login",
  password="W1ww6y2c",
  database="user8745_login"
)
mycursor = mydb.cursor()

@route('/')
def hello():
    return "Hello World!"

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
    sql = "SELECT password FROM users_login WHERE login = %s" 
    mycursor.execute(sql,username)
    sql_password = mycursor.fetchall()
    return "<p>{}<p>".format(sql_password)
    if check_login(username, password):
        return "<p>Вы ввели проавильный логин и пароль.</p>"
    else:
        return "<p>Неправильный логин или пароль.</p>"
run(host='localhost', port=8080, debug=True)