from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with

app = Flask(__name__)
app.config['SECRET_KEY'] = '2d4904a0818e55ebf6d4c38e8af9b56c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)
bcrypt = Bcrypt(app)

from project import routes__