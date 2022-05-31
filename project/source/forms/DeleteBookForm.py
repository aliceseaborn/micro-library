# DELETE BOOK

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


class DeleteBookForm(FlaskForm):
	delete = SubmitField('Delete')
