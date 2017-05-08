from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default=False)


class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = PasswordField('password', validators=[DataRequired()])
    itemName = PasswordField('password', validators=[DataRequired()])
    addr = BooleanField('Remember_me', default=False)