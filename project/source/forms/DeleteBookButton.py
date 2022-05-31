# DELETE BOOK

from flask_wtf import FlaskForm
from wtforms.fields import SubmitField


delete_style={'type': 'button', 'class': 'btn btn-danger'}

class DeleteBookButton(FlaskForm):
	delete = SubmitField('Delete', render_kw=delete_style)
