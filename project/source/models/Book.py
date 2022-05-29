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
	year = db.Column(db.DateTime)
	available = db.Column(db.Boolean)
	isbn = db.Column(db.String(16), unique=True)
	tags = db.Column(db.Text)
	
	def __init__(self, data):
		self.title = data["title"]
		self.author = data["author"]
		self.fiction = self._process_boolean(data["fiction"])
		self.year = self._process_year(data["year"])
		self.subject = data["subject"]
		self.synopsis = data["synopsis"]
		self.isbn = data["isbn"]
		self.available = self._process_boolean(data["available"])
		self.tags = data["tags"]
		
	def __repr__(self):
		return f"<Book {self.isbn} by {self.author}.>"
	
	def _process_boolean(self, data):
		if data == "True": return True
		else: return False

	def _process_year(self, data):
		return datetime(data, 1, 1)

