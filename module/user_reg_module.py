from bottle import get, post, request # or route

@get('/reg')
def login():
    return '''
        <form action="/reg" method="post">
            Логин: <input name="username" type="text" />
            Пароль: <input name="password" type="password" />
            Потверждение пароля: <input name="password-correct" type="password" />
            <p>Введите пожалуйста номер телефона в формате +996(555)123456
            Номер телефона: <input name="phone_number" type="text" />
            <input value="Login" type="Регистрация" />
        </form>
    '''

@post('/reg') 
def do_login():
    username = request.forms.get('username')
    password-correct = request.forms.get('password-correct')
    password = request.forms.get('password')
    
    if check_login(username, password):
        return "<p>Вы ввели проавильный логин и пароль.</p>"
    else:
        return "<p>Неправильный логин или пароль.</p>"

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Логин: <input name="username" type="text" />
            Пароль: <input name="password" type="password" />
            <input value="Login" type="Вход" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Вы ввели проавильный логин и пароль.</p>"
    else:
        return "<p>Неправильный логин или пароль.</p>"