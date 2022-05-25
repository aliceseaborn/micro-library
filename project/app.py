# APP

from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from flask_flatpages import pygments_style_defs

from source import app, db, pages
from source.models.User import User
from source.forms.LoginForm import LoginForm
from source.forms.RegisterForm import RegisterForm


# ------------------------------ FLASK ROUTES ------------------------------ #

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/wiki')
def wiki():
	return render_template('wiki.html', pages=pages)

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
