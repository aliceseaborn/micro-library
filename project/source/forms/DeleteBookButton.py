# DELETE BOOK

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class DeleteBookButton(FlaskForm):
	delete = SubmitField('Delete')
