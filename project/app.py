# APP

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from flask_flatpages import pygments_style_defs

from source import app, db, pages
from source.config import (JSON_BOOK_DATA_PATH, SUBJECTS,
	CATEGORIES, AVAILABILITIES)

from source.models.User import User
from source.models.Book import Book

from source.forms.LoginForm import LoginForm
from source.forms.RegisterForm import RegisterForm
from source.forms.AddBookForm import AddBookForm
from source.forms.AddBookButton import AddBookButton
from source.forms.DeleteBookButton import DeleteBookButton
from source.forms.EditBookButton import EditBookButton
from source.forms.EditBookForm import EditBookForm


# ------------------------------ FLASK ROUTES ------------------------------ #

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/wiki')
def wiki():
	return render_template('wiki.html', pages=pages)

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
	form = AddBookButton()
	if form.validate_on_submit():
		return redirect(url_for('addbook'))
	books = db.session.query(Book).all()
	return render_template('inventory.html', books=books, form=form)

@app.route('/addbook', methods=['GET', 'POST'])
def addbook():
	form = AddBookForm()
	if form.validate_on_submit():
		book = Book(title=form.title.data,
					author=form.author.data,
					category=form.category.data,
					year=form.year.data,
					subject=form.subject.data,
					synopsis=form.synopsis.data,
					isbn=form.isbn.data,
					status=form.status.data,
					tags=form.tags.data)
		db.session.add(book)
		db.session.commit()
		flash(f"{form.title.data} has been added to the database.")
		return redirect(url_for('inventory'))
	return render_template('addbook.html', form=form)

@app.route('/delete_book', methods=['GET','POST'], defaults={'isbn': "0000000000"})
def delete_book(isbn  = "0000000000"):
	if 'isbn' in request.args:
		isbn = request.args['isbn']
	Book.query.filter(Book.isbn==isbn).delete()
	db.session.commit()
	flash(f"The selected book has been removed from the database.")
	return redirect(url_for('inventory'))

@app.route('/edit_book', methods=['GET','POST'], defaults={'isbn': "0000000000"})
def edit_book(isbn  = "0000000000"):
	if 'isbn' in request.args:
		isbn = request.args['isbn']
	form = EditBookForm()
	book = Book.query.filter(Book.isbn==isbn).first()
	if form.validate_on_submit():

		Book.query.filter(Book.isbn==isbn).update({
				"title": form.title.data,
				"author": form.author.data,
				"category": form.category.data,
				"year": form.year.data,
				"subject": form.subject.data,
				"synopsis": form.synopsis.data,
				"isbn": form.isbn.data,
				"status": form.status.data,
				"tags": form.tags.data
			})
		db.session.commit()
		flash(f"Details of {book.title} have been updated in the database.")
		return redirect(url_for('inventory'))
	return render_template('editbook.html', form=form, book=book,
		subjects=SUBJECTS, categories=CATEGORIES, availabilities=AVAILABILITIES)

@app.route('/book', methods=['GET', 'POST'], defaults={'isbn': "0000000000"})
def book(isbn = "0000000000"):
	if 'isbn' in request.args:
		isbn = request.args['isbn']
	delete_form = DeleteBookButton(request.form, prefix="delete_book")
	edit_form = EditBookButton(request.form, prefix="edit_book")
	if delete_form.validate_on_submit():
		return redirect(url_for('delete_book') + f"?isbn={isbn}")
	if edit_form.validate_on_submit():
		return redirect(url_for('edit_book') + f"?isbn={isbn}")
	book = Book.query.filter_by(isbn=isbn).first()
	return render_template('book.html', book=book, delete_form=DeleteBookButton(),
		edit_form=EditBookButton())

@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thank you for registering!')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user.check_password(form.password.data) and user is not None:
			login_user(user)
			flash('Logged in successfully.')
			next = request.args.get('next')
			if next == None or not next[0]=='/':
				next = url_for('index')
			return redirect(next)
	return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have successfully logged out.')
	return redirect(url_for('index'))

@app.route('/<path:path>')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)

@app.route('/pygments.css')
def pygments_css():
	return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}


# ---------------------------------- MAIN ---------------------------------- #

if __name__ == '__main__':
	app.run()
