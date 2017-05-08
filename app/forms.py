from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Remember_me', default=False)


class RecordForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = PasswordField('password', validators=[DataRequired()])
    item_name = PasswordField('itemName', validators=[DataRequired()])
    type = StringField('type',default='M')
    addr = StringField('addr', default=False)