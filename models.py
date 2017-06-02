from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/idered'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    '''
    Table user
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(254), nullable=False, unique=True)
    password = db.Column(db.String(106), nullable=False, unique=False)
    is_active = db.Column(db.Boolean)
    token = db.Column(db.String(32), nullable=False, unique=False)
    # 1 Admin, 2 Teacher, 3 Admin
    rol = db.Column(db.Integer)
    

    def __init__(self):
        self.is_active = False
        self.token = str(uuid4()).replace('-', '')
        self.rol = 3

    def __repr__(self):
        return '<User %r>' % self.username