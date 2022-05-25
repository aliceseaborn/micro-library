# REGISTERFORM

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


email_style={'type': 'email', 'class': 'form-control'}
password_style={'type': 'password', 'class': 'form-control'}


class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()],
    	render_kw=email_style)
    password = PasswordField('Password', validators=[DataRequired(),
    	EqualTo('pass_confirm', message='Passwords Must Match!')],
    	render_kw=password_style)
    pass_confirm = PasswordField('Confirm password',
    	validators=[DataRequired()], render_kw=password_style)
    submit = SubmitField('Submit')

    def check_email(self, field):
        # Check if not None for that user email!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('An account with this email address already exists.')

