#coding=utf-8
from flask import Flask,render_template,redirect,url_for
from app import app
from flask import request

# return redirect(url_for('show_entries'))


@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user', methods = ['GET', 'POST'])
def user():
    username = request.form['username']
    pwd = request.form['password']
    if(pwd=='1'):
        return redirect(url_for('index'))
    user = {'nickname': 'Miguel'}  # 用户名
    posts = [  # 提交内容
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('t.html',title = 'Home',
                               user = user,
                               posts = posts)
