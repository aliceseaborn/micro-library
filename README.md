# Micro Library

A small web app for managing a micro library. Includes a Flask front-end and a SQL database backend for tracking the availability of books, when books are due, and who has rented them.

Core features:
- QR codes on the books link to the site
- Books can be checked out by account holders
- Automatic email reminders when books are due
- An index available to display the current offerings
- The ability to extend the lease on a book up to a specified number of days

If running this application for the first time, please follow the commands below in your shell prompt:
```BASH
conda create -y -n micro-library --file conda-spec.txt
pip install -r requirements.txt
export FLASK_ENV=development
export FLASK_APP=app.py
flask db init
flask db migrate
flask db upgrade
flask run
````


*alice seaborn.*
