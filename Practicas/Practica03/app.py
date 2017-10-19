# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask import url_for, escape, request, session, redirect


app = Flask(__name__)



#lista = ["Uno","Dos","Tres"]

@app.route('/')                         # decorador, varia los parametros
def principal():
    user = None
    lista = None
    if 'user' in session and 'last' in session:
        user = session['user']
        lista = session['last']
        lista.append("/")
        session['last'] = lista[-2:]
    return render_template('./hija.html',usuario=user,rows=lista)

@app.route('/otra')                         # decorador, varia los parametros
def otro():
    user = None
    lista = None
    if 'user' in session and 'last' in session:
        user = session['user']
        lista = session['last']
        lista.append("/otra")
        session['last'] = lista[-2:]
    return render_template('./hija.html',usuario=user,rows=lista)


@app.route('/ruta')                         # decorador, varia los parametros
def ruta():
    user = None
    lista = None
    if 'user' in session and 'last' in session:
        user = session['user']
        lista = session['last']
        lista.append("/ruta")
        session['last'] = lista[-2:]
    return render_template('./hija.html',usuario=user,rows=lista)









@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['user']
        session['last'] = []
    return redirect(url_for('principal'))


@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('user', None)
    session.pop('last',None)
    return redirect(url_for('principal'))




app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
