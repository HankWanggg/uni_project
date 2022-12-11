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
    firstName = db.Column('first_name',db.String(20), nullable=False)
    lastName = db.Column('last_name',db.String(20), nullable=False)
    userName = db.Column('username',db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    
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
    mark = db.Column(db.Integer, nullable=False)
   #students dont need username and password
    
    def __init__(self,firstName,lastName,userName,password):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.password = password
        self.mark = 0
    def __repr__(self):
        return f'<Student "{self.firstName + self.lastName}">'        
class Course(db.Model):
    id = db.Column('course_id', db.Integer, nullable=False, primary_key=True)
    courseName = db.Column('course_name', db.String(20), unique=True, nullable=False)
    professor_id = db.Column('professor_id',db.Integer, db.ForeignKey('professor.professor_id',), nullable=False)
    professor = db.relationship('Professor',backref=db.backref('professor'))
    def __init__(self,courseName,professor_id):
        self.courseName = courseName
        self.professor_id = professor_id
    def __repr__(self):
        return f'<Course "{self.courseName}">'     
class Menu(db.Model):
    id = db.Column('id', db.Integer, nullable=False, primary_key=True)
    menuText = db.Column('menu_text', db.String(30), unique=True, nullable=False)
    acronym = db.Column(db.String(20), unique=True, nullable=False)
    
    def __init__(self,menuText,acronym):
        self.menuText = menuText
        self.acronym = acronym
    def __repr__(self):
        return f'<Menu "{self.acronym}">'     
    # work
def update_professor(userName,password,professorId):
    update = Professor.query.filter_by(id=professorId).first()
    update.userName = userName
    update.password = password
    db.session.commit()
    
    # work
def insert_professor(firstName,lastName,userName,password):
    data = Professor(firstName, lastName, userName, password)     
    db.session.add(data)
    db.session.commit()
    
   
   # work 
def update_student(firstName,studentId):
    update = Student.query.filter_by(id=studentId).first()
  
    update.firstName =firstName
    db.session.commit()
    
    # work
def update_student_mark(mark,studentId):
    update = Student.query.filter_by(id=studentId).first()
  
    update.mark =update.mark + mark
    db.session.commit()
    
    # work
def insert_student(firstName,lastName,userName,password):
    data = Student(firstName, lastName, userName,password)     
    db.session.add(data)
    db.session.commit()

def update_course():
    update = Student.query.filter_by(id=db.Integer).first()
    update.courseName = courseName
    db.session.commit()

def insert_course(courseName,professor_id):
    
    data = Course(courseName,professor_id)     
    db.session.add(data)
    db.session.commit()


     