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
	fiction = db.Column(db.Boolean)
	year = db.Column(db.String(4))
	available = db.Column(db.Boolean)
	isbn = db.Column(db.String(16), unique=True)
	tags = db.Column(db.Text)
	
	def __init__(self, title, author, fiction, year,
		subject, synopsis, isbn, available, tags):
		self.title = title
		self.author = author
		self.fiction = self._process_boolean(fiction)
		self.year = year
		self.subject = subject
		self.synopsis = synopsis
		self.isbn = isbn
		self.available = self._process_boolean(available)
		self.tags = tags
		
	def __repr__(self):
		return f"<Book {self.isbn} by {self.author}.>"
	
	def _process_boolean(self, data):
		if data == "True": return True
		else: return False

