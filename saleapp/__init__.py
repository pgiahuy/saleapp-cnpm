from flask_sqlalchemy import SQLAlchemy
from flask import  Flask
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)