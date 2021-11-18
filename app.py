from flask import Flask
from flask_restful import Resource, Api
from pkgutil import iter_modules
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+mysqlconnector://root:@localhost/midterm"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api = Api(app)

db = SQLAlchemy(app)

