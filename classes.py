from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

user='root' 
password='hankang0603'
host='127.0.0.1'
database='uniproject'

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
    def __repr__(self):
        return f'<Professor "{self.firstName + self.lastName}">'
        
 # work 
class Student(db.Model):
    id = db.Column('student_id', db.Integer, nullable=False, primary_key = True)
    firstName =  db.Column('first_name',db.String(20), nullable=False)
    lastName = db.Column('last_name',db.String(20), nullable=False)
    userName = db.Column('username',db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    def __init__(self,firstName,lastName,userName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
    def __repr__(self):
        return f'<Student "{self.firstName + self.lastName}">'        
class Course(db.Model):
    id = db.Column('course_id', db.Integer, nullable=False, primary_key=True)
    courseName = db.Column(db.String(20), unique=True, nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professor.professor_id'), nullable=False)
    
    def __init__(self,courseName,professor_id):
        self.courseName = courseName
        self.professor_id = professor_id
    def __repr__(self):
        return f'<Course "{self.courseName}">'     
    
def update_professor():
    update = Student.query.filter_by(id=db.Integer).first()
    update.userName = 'newusername'
    update.password = 'newpassword'
    db.session.commit()
    
def insert_professor(firstName,lastNme,userName,password):
    data = Professor('firstName', 'lastName', 'userName', 'password',)     
    db.session.add(data)
    db.seesion.commit()
    
   
   # work 
def update_student(firstName,studentId):
    update = Student.query.filter_by(id=studentId).first()
  
    update.firstName =firstName
    db.session.commit()
    
    # work
def insert_student(firstName,lastName,userName,password):
    data = Student(firstName, lastName, userName,password)     
    db.session.add(data)
    db.session.commit()

def update_course():
    update = Student.query.filter_by(id=db.Integer).first()
    update.courseName = 'newcoursename'
    db.session.commit()

def insert_course(courseName):
    data = Course('courseName')     
    db.session.add(data)
    db.seesion.commit()


    
