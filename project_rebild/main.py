#!/usr/bin/python3.5.2
# -*- coding: utf8 -*-
import json
import uuid
import datetime
import os

from bottle import Bottle,route, request, static_file, run, get, post, abort, SimpleTemplate,template,response
application  = Bottle()

import mysql.connector

mydb = mysql.connector.connect(
  host="176.126.165.135",
  user="user8745_login",
  password="W1ww6y2c",
  database="user8745_login",
)
@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_password(username, password):
        response.set_cookie("account", username, secret='some-secret-key')
        return template("<p>Добро пожаловать {{name}}! Вы не авторизованы.</p>", name=username)
    else:
        return "<p>Авторизация не удалась.</p>"
    
def check_password(username,password):
    return True

@route('/restricted')
def restricted_area():
    username = request.get_cookie("account", secret='some-secret-key')
    if username:
        return template("Привет {{name}}. Добро пожаловать.", name=username)
    else:
        return "Вы не авторизованы. Доступ запрещён."


run(host='localhost', port=8080, debug=True)
