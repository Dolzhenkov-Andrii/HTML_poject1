"""
  Server
"""

from flask import Flask
from flask_cors import CORS, cross_origin
# from appli import posts
from appli import photos
from config.db import DB_URI, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app, support_credentials=True)


# app.register_blueprint(posts.posts, url_prefix='/api/')
app.register_blueprint(photos.photos ,url_prefix='/api/')

if __name__=="__main__":
    app.run('127.0.0.1',5050, debug=True)
