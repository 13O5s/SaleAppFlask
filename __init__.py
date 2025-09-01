from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote


app = Flask(__name__)
password = quote("admin@123")
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{password}@localhost/saledbv2?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# password = quote("flaskpass123")
# app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://flaskuser:{password}@localhost/saledbv2?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app = app)
