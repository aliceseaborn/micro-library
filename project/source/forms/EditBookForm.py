# EDIT BOOK FORM

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


text_style={'type': 'text', 'class': 'form-control'}

class EditBookForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()],
		render_kw=text_style)
	author = StringField('Author', validators=[DataRequired()],
		render_kw=text_style)
	category = StringField('Category', validators=[DataRequired()],
		render_kw=text_style)
	year = StringField('Year Published', validators=[DataRequired()],
		render_kw=text_style)
	subject = StringField('Subject', validators=[DataRequired()],
		render_kw=text_style)
	synopsis = TextAreaField('Synopsis', validators=[DataRequired()], 
		render_kw=text_style)
	isbn = StringField('ISBN', validators=[DataRequired()], 
		render_kw=text_style)
	status = StringField('Status', validators=[DataRequired()],
		render_kw=text_style)
	tags = StringField('Tags', validators=[DataRequired()], 
		render_kw=text_style)
	submit = SubmitField('Submit')

