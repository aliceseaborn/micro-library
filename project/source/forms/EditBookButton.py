# EDIT BOOK BUTTON

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class EditBookButton(FlaskForm):
	edit = SubmitField('Edit Book')
