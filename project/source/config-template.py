# CONFIG

import os


DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = ".md"
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'tables', 'markdown_katex', 'footnotes']

SECRET_KEY = "something secret thisway comes..."

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db/data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
