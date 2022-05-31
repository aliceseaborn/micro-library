# ADDBOOKFORM

from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField, SelectField, TextAreaField)
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError


text_style={'type': 'text', 'class': 'form-control'}
choices = dict({
	"subject": [('History','History'),('biography','Biography')],
	"fiction": [("True",'Fiction'),("False",'Non-Fiction')],
	"available": [("True",'Available'),("False",'Not Available')]
})


class AddBookForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired()],
		render_kw=text_style)
	author = StringField('Author', validators=[DataRequired()],
		render_kw=text_style)
	fiction = SelectField('Fiction', validators=[DataRequired()],
		render_kw=text_style, choices=choices['fiction'])
	year = StringField('Year Published', validators=[DataRequired()])
	subject = SelectField('Subject', validators=[DataRequired()],
		render_kw=text_style, choices=choices['subject'])
	synopsis = TextAreaField('Synopsis', validators=[DataRequired()], 
		render_kw=text_style)
	isbn = StringField('ISBN', validators=[DataRequired()], 
		render_kw=text_style)
	available = SelectField('Availability', validators=[DataRequired()],
		render_kw=text_style, choices=choices['available'])
	tags = StringField('Tags', validators=[DataRequired()], 
		render_kw=text_style)
	submit = SubmitField('Submit')

	def check_isbn(self, field):
		if Book.query.filter_by(isbn=field.data).first():
			raise ValidationError('A book with this ISBN already exists.')

