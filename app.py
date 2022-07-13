"""
  Server
"""
from flask import Flask
from appli.posts import posts
from appli.photos import photos

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
app.register_blueprint(photos)
# app.config["APPLICATION_ROOT"] = "/api"

@app.route('/')
def get():
    return {'post':'2','name':'Tonya'}

if __name__=="__main__":
    app.run(host='127.0.0.1', port=5050, debug=True)
