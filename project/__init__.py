from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrybt = Bcrypt(app)
login_manager = LoginManager(app)

"""
This is the main application module for the Flask app.
It initializes the Flask app, SQLAlchemy, Bcrypt, and LoginManager.
"""

from project import routes
