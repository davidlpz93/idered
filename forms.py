from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired('Campo obligatorio'),
        Email('Formato no válido')
        ])
    password = PasswordField('Contraseña', validators=[
        DataRequired('No me has indicado una contraseña')
        ])
 
