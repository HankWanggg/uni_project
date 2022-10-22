from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

user='root' 
password='hankang0603'
host='127.0.0.1'
database='MySQL'

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://'+user+':'+password+'@'+host+"/"+database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

db = SQLAlchemy(app)

