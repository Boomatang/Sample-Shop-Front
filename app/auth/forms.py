from flask_wtf import Form
from wtforms import StringField, SelectField, IntegerField, BooleanField, DecimalField, FileField, TextAreaField, \
    PasswordField, SubmitField
from wtforms.validators import data_required, Length, Email, Regexp, EqualTo, ValidationError

from ..model import User


class AddProduct(Form):
    name = StringField('Product Name', validators=[data_required()], description="Product Name")
    description = TextAreaField("Product Description", description='Product Description')
    image = FileField('Image Field')
    cost = DecimalField('Price', places=2, description="000.00")
    active = BooleanField('Active')


class RegistrationForm(Form):
    email = StringField('Email', validators=[data_required(), Length(1, 64),
                                             Email()])
    email2 = StringField('Confirm Email', validators=[data_required(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        data_required(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                               'Usernames must have only letters, '
                                               'numbers, dots or underscores')])
    password = PasswordField('Password', validators=[
        data_required(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[data_required()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class LoginForm(Form):
    email = StringField('Email', validators=[data_required(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[data_required()])
    remember_me = BooleanField('Remember me')
