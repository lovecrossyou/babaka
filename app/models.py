#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

# 用户表
class User(db.Model):
    """每一个属性定义一个字段"""
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    addr = db.Column(db.String(120), index = True, unique = True)
    phone = db.Column(db.String(120), index = True, unique = True)
    sex = db.Column(db.String(12), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)
    def __repr__(self):
        return '<User %r>' % (self.nickname)

# 商品表
class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    type = db.Column(db.String(120), index=True, unique=True)
    def __repr__(self):
        return '<Item %r>' % (self.name)

# 记录表
class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(120), index=True, unique=True)
    extral = db.Column(db.String(120), index=True, unique=True)
    addr = db.Column(db.String(120), index=True, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    def __repr__(self):
        return '<Item %r>' % (self.addr)