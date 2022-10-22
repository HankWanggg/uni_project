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

class Professor(db.Model):
    id = db.Column('professor_id', db.Integer, nullable=False, primary_key = True)
    firstName = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    courses = db.relationship('Course', backref='professor')
    
    def __init__(self,firstName,lastName,userName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password            
        return f'<Professor "{self.firstName}">'
        
  
class Student(db.Model):
    id = db.Column('student_id', db.Integer, nullable=False, primary_key = True)
    firstName =  db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(20), nullable=False)
    userName = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    def __init__(self,firstName,lastName,userName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        
class Course(db.Model):
    id = db.Column('course_id', db.Integer, nullable=False, primary_key=True)
    courseName = db.Column(db.String(20), unique=True, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.id'))
    
    def __init__(self,courseName,professor_id):
        self.courseName = courseName
        self.professor_id = professor_id
        return f'<Course "{self.courseName}">'
    
    
def update_professor(firstName, lastName, userName, password):
    from classes import Professor
    from classes import db
    data = Professor('firstName', 'lastName', 'userName, 'password') 
    
def insert_professor():
    pass

def update_student():
    pass

def insert_student():
    pass

def update_course():
    pass

def insert_coourse():
    pass




        #def changePassword(self,newPassword):
            #self.password = newPassword
                
        
        #p1 = professor('abcf','abcl','abcu','abcp')
        #p2 = professor('2abcf','2abcl','2abcu','2abcp')
            
        #print(p1.password)
        #p1.changePassword('def')
            
        #print(p1.password)        