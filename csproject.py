
from classes import *
import random
from mysql.connector import (connection)
ATTANDANCE = 'ATTANDANCE'
REVIEW_CHART = 'REVIEW_CHART' 

cnx = connection.MySQLConnection(user='root', password='hankang0603',
                                 host='127.0.0.1',
                                 database='MySQL')

def checkUserNameAndPassword(Username,Password,Password1):
    if  Password1 != Password:
        print("Passwords don't match, please try again")
        return False
    elif len(Password)<8:
        print("Your password should be at least 8 digits, please enter aonther password")
        return False
 
    elif Professor.query.filter_by(userName=Username).first() is not None:
        print("Username exists")
        return False       
    else:
        insert_professor(Firstname,Lastname,Username,Password)
        print("Success!")  
        return True
#add register ur first and last name
def register(): 
    Firstname = input("Enter your firstname:")
    Lastname = input("Enter your lastname:")
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Comfirm password:")    
    with app.app_context():     
        if(not checkUserNameAndPassword(Username,Password,Password1)):
            register()
            

def access():
    Username = input("Enter your username:")
    Password = input("Enter your password:") 
    if  len(Username)>1  and len(Password)>1:
        with app.app_context():
            professorFound = Professor.query.filter_by(userName=Username).first() 
        if professorFound is None:
            loginSuccess = False
            print("Password or Username incorrect") 
            access()  
        else:
           
            if (professorFound.password == Password):
                print("Login success")
                print("Hi,", Username)     
                loginSuccess = True    
            else:
                
                loginSuccess = False
                print("Password or Username incorrect") 
                access()                                 
     
    else:
        print("Please enter a value")
        access()
            

        
   
        
     
def displayMenu():
    with app.app_context():
          
        menus = Menu.query.all()
        menuList = []
        for menu in menus:
            print(str(menu.id) + ':'+menu.menuText)
            menuList.append(str(menu.id))
        userInput = input('enter an option')
        
        while userInput not in menuList:
            userInput = input('enter an option')
        return userInput        
    
def handleOption(userInputOption):
    with app.app_context():
        selectedOption =Menu.query.filter_by(id=int(userInputOption)).first()
        
    if selectedOption.acronym == ATTANDANCE:
        with app.app_context():
            #select all 
            students = Student.query.all()
           # random pick
            pickedStudents = random.sample(students,k=3)
            for stu in pickedStudents:
                update_student_mark(1,stu.id)
                print(stu.userName +' mark is now:' + str(stu.mark))
          #  select one  search by
                    
        
        
    elif selectedOption.acronym == REVIEW_CHART:
        with app.app_context():
            
            students = Student.query.all()
         
            for stu in students: 
                print(stu.userName +' mark is now:' + str(stu.mark))        
        
       
 
    
    
def home(option=None):
    option = input("Login | Signup:")
    if option.lower() == "login":
        access()
    elif option.lower() == "signup":
        register()
    else:
        print("Please enter an option")
        home()
    userInputOption = displayMenu()
    handleOption(userInputOption)
    
if __name__ == '__main__':
    home()
