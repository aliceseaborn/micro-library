# ADD BOOK BUTTON

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class AddBookButton(FlaskForm):
	add = SubmitField('Add Book')
