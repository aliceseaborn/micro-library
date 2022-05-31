# BOOK

from datetime import datetime
import json

from source import db


class Book(db.Model):
	__tablename__ = "books"
	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	author = db.Column(db.String(64))
	subject = db.Column(db.String(16))
	synopsis = db.Column(db.Text)
	category = db.Column(db.String(5))
	year = db.Column(db.String(4))
	status = db.Column(db.String(5))
	isbn = db.Column(db.String(16), unique=True)
	tags = db.Column(db.Text)
	
	def __init__(self, title, author, category, year,
		subject, synopsis, isbn, status, tags):
		self.title = title
		self.author = author
		self.category = category
		self.year = year
		self.subject = subject
		self.synopsis = synopsis
		self.isbn = isbn
		self.status = status
		self.tags = tags
		
	def __repr__(self):
		return f"<Book {self.isbn} by {self.author}.>"

