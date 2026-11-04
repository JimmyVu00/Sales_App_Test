from tempfile import template

from flask import Flask, template_rendered
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'cacccccccevsdfsfwedsse@$@$#'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 2
db = SQLAlchemy(app=app)
