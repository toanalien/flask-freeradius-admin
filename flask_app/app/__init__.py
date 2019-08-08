from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
admin = Admin(app)

from app import radius_models
from app import routes