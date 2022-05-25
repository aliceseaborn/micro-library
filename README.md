# Micro Library

A small web app for managing a micro library. Includes a Flask front-end and a SQL database backend for tracking the availability of books, when books are due, and who has rented them.

Core features:
- QR codes on the books link to the site
- Books can be checked out by account holders
- Automatic email reminders when books are due
- An index available to display the current offerings
- The ability to extend the lease on a book up to a specified number of days

If running this application for the first time, start by creating a new conda environment and installing the dependencies.
```BASH
conda create -y -n micro-library --file=conda-spec.txt python
conda activate micro-library
pip install -r requirements.txt
````

Within `project/source/`, rename `config-template.py` to `config.py` and generate a new alphanumeric secret key by running the command below. Copy and paste that key inside the new config file for the `SECRET_KEY` variable.
```BASH
cat /dev/urandom | tr -dc '[:alpha:]' | fold -w ${1:-32} | head -n 1
```

Initialize the application database and point Flask to the application file.
```BASH
cd project/
export FLASK_ENV=development
export FLASK_APP=app.py
flask db init
flask db migrate
flask db upgrade
````

Once the database is initialized, you are ready to run the app with flask. By default, the webapp will run on the machine under port 5000. If you are running the app on a personal computer, you can use the webapp by visiting [http://localhost:5000/](http://localhost:5000/) in a web browser.
```BASH
flask run
````



*alice seaborn.*
