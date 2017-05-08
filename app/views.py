#coding=utf-8
from flask import Flask,render_template,redirect,url_for
from app import app
from app.forms import LoginForm
from flask import request


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',form=form)


@app.route('/user', methods = ['GET', 'POST'])
def user():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        return redirect('/')
    return redirect(url_for('index'))

