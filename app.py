"""
  Server
"""
from flask import Flask
from flask_cors import CORS, cross_origin

from appli import posts
from appli import photos

from databases.connection import Connection
from databases.managers.base import BaseManager
from config.db import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER

connection = Connection(
    DB_HOST,
    DB_USER,
    DB_PASSWORD,
    DB_NAME)
BaseManager.database_connection = connection._connection


app = Flask(__name__)
CORS(app, support_credentials=True)
app.register_blueprint(posts.posts, url_prefix='/api/')
app.register_blueprint(photos.photos ,url_prefix='/api/')


if __name__=="__main__":
    app.run('127.0.0.1',5000, debug=True)
