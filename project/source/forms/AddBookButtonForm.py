# ADD BOOK BUTTON

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class AddBookButtonForm(FlaskForm):
	add = SubmitField('Add Book')
