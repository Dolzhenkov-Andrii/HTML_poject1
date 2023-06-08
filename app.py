'''
    Server
'''

from flask import Flask
from flask_cors import CORS
from routes import (
    posts,
    registration,
    users,
    photos,
    authorization,
    # images
)
from config.db import DB_URI, db
from config.config import APP_PORT, APP_HOST

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
CORS(app,
    resources={r'/*': {'origins': 'http://localhost:3000'}},
    upport_credentials=True,
    methods=['POST', 'GET'],
    support_credentials=True
    )

app.register_blueprint(registration.registration, url_prefix='/api/')
app.register_blueprint(authorization.author, url_prefix='/api/')
app.register_blueprint(users.users, url_prefix='/api/')
app.register_blueprint(posts.posts, url_prefix='/api/')
app.register_blueprint(photos.photos, url_prefix='/api/')
# app.register_blueprint(images.images, url_prefix='/api/')


if __name__ == '__main__':
    app.run(APP_HOST, APP_PORT, debug=True)
