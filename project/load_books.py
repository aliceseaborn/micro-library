# LOAD BOOKS

from json import load

from source import db
from source.config import JSON_BOOK_DATA_PATH
from source.models.Book import Book


with open(JSON_BOOK_DATA_PATH) as file:
	data = load(file)
	file.close()
book_objects = []
for book_json in data["books"]:
	new_book = Book(
		title = book_json["title"],
		author = book_json["author"],
		category = book_json["category"],
		year = book_json["year"],
		subject = book_json["subject"],
		synopsis = book_json["synopsis"],
		isbn = book_json["isbn"],
		status = book_json["status"],
		tags = book_json["tags"]
	)
	book_objects.append(new_book)
db.session.add_all(book_objects)
db.session.commit()

