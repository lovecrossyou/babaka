#coding=utf-8
from flask import Flask,render_template
from app import app
from forms import LoginForm


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

@app.route('/login', methods = ['GET', 'POST'])
def login():
        form = LoginForm()
        return render_template('login.html',
            title = 'Sign In',
            form = form)

@app.route('/user', methods = ['GET', 'POST'])
def user():
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
