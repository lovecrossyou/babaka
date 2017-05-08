#coding=utf-8
from flask import Flask,render_template,redirect,url_for
from app import app
from app.forms import LoginForm,RecordForm
from flask import request
from app.models import Item

@app.route('/')
def index():
    # 请求记录数据
    # 加载商品类型
    items = Item.query.all()
    print(items)
    return render_template('index.html',items=items)

# 登录
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


@app.route('/additem')
def addItem():
    name = request.form['name']
    phone = request.form['phone']
    sex = request.form['sex']
    addr = request.form['addr']
    type = request.form['type']
    item_name = request.form['item_name']


    return redirect(url_for('index'))



# 未找到页面
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404

