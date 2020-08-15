from bottle import route, run, template, static_file, post, request, get, post, redirect, response
import os.path, os, hashlib, datetime, sqlite3

print(os.path)
db = 'C:\\GitHub\\sms-tender\\auth_git_hub\\bottle-auth-test-master\\inky.sqlite'


@route('/')
def main():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
        <p>Or sign up</p>
        <form action="/signup" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            Email: <input name="email" type="email" />
            <input value="Sign Up" type="submit" />
        </form>
    '''


@route('/profile/<user>')
def profile(user):
    is_logged_in()
    return template('profile',username=user)

@route('/signup', method='POST')
def sign_up():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if not select_user(username):
        ts = datetime.datetime.now()+datetime.timedelta(days=1)
        pwhash = hashlib.md5()
        pwhash.update(password)
        session_id = hashlib.md5()
        session_id.update(str(ts))
        response.set_cookie('user',username,expires=ts)
        response.set_cookie('session',session_id.hexdigest(),expires=ts)
        new_user(username,pwhash.hexdigest(),session_id.hexdigest())
        redirect('/profile/'+username)
    else:
        return '<p>Username already exists</p><p>Return <a href="/">HOME</a></p>'


@post('/login', method='POST')
def log_me_in():
    username = request.forms.get('username')
    password = request.forms.get('password')
    pwhash = hashlib.md5()
    pwhash.update(password)
    if verify_login(username,pwhash.hexdigest()):
        ts = datetime.datetime.now()+datetime.timedelta(days=1)
        session_id = hashlib.md5()
        session_id.update(str(ts))
        create_session_db(username,session_id.hexdigest())
        response.set_cookie('user',username,expires=ts)
        response.set_cookie('session',session_id.hexdigest(),expires=ts)
        redirect('/profile/'+username)
    else:
        return '<p>Login Failed</p><p>Return <a href="/">HOME</a></p>'

@route('/logout')
def logout():
    username = request.get_cookie("user")

    logout_user_db(username)

    response.delete_cookie("user")
    response.delete_cookie("session")
    redirect('/')

def is_logged_in():
    if request.get_cookie("user") != None:
        un = request.get_cookie("user")
        udata = select_user(un)
        if un == udata["username"]:
            if udata["session_id"] != request.get_cookie("session"):
                redirect('/')
        else:
            redirect('/')

def verify_login(un,pw):
    udata = select_user(un)
    if udata:
        if pw == udata['password']:
            return True
    return False


def check_and_build_db():
    if not os.path.isfile(db):
        db_conn = sqlite3.connect('C:\GitHub\sms-tender\auth_git_hub\bottle-auth-test-master')
        c = db_conn.cursor()
        c.execute("CREATE TABLE users (username text PRIMARY KEY, password text NOT NULL,session_id text DEFAULT null)")
        db_conn.commit()
        db_conn.close()

def select_user(user):
    db_conn = sqlite3.connect(db)
    c = db_conn.cursor()
    c.execute('''SELECT username, password, session_id FROM users WHERE username=?''',(user,))
    row_data = c.fetchone()
    if row_data is None:
        return False
    user_data = {"username":row_data[0],"password":row_data[1],"session_id":row_data[2]}
    db_conn.close()
    return user_data

def logout_user_db(user):
    db_conn = sqlite3.connect(db)
    c = db_conn.cursor()
    c.execute('''UPDATE users SET session_id = NULL WHERE username=?''',(user,))
    db_conn.commit()
    db_conn.close()

def create_session_db(user,session):
    db_conn = sqlite3.connect(db)
    c = db_conn.cursor()
    c.execute('''UPDATE users SET session_id=? WHERE username=?''',(session,user))
    db_conn.commit()
    db_conn.close()

def new_user(un,pw,sid):
    db_conn = sqlite3.connect(db)
    c = db_conn.cursor()
    c.execute('''INSERT INTO users(username,password,session_id) VALUES(?,?,?)''',(un,pw,sid))
    db_conn.commit()
    db_conn.close()


#####---------------------------Run-the-server-----------------------------#####
if __name__ == '__main__':
    check_and_build_db()
    run(host='localhost', port=8080)
