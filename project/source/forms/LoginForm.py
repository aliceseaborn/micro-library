# LOGINFORM

from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


email_style={'type': 'email', 'class': 'form-control'}
password_style={'type': 'password', 'class': 'form-control'}


class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()],
		render_kw=email_style)
	password = PasswordField('Password', validators=[DataRequired()],
		render_kw=password_style)
	submit = SubmitField('Submit')

