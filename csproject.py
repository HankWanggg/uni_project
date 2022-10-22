import classes

from mysql.connector import (connection)
ATTANDANCE = 'ATTANDANCE'
REVIEW_CHART = 'REVIEW_CHART'
S_COURSE_SCORE = 'S_COURSE_SCORE'

cnx = connection.MySQLConnection(user='root', password='hankang0603',
                                 host='127.0.0.1',
                                 database='MySQL')


def register():

    professorUsernamePasswordQuery = "select professor_id, username from uniproject.professor"
    mycursor = cnx.cursor()
    mycursor.execute(professorUsernamePasswordQuery)
    myresult = mycursor.fetchall()
    userNameList = []
    userIdList = []
    for row in myresult:
        userIdList.append(row[0])
        userNameList.append(row[1])
        
   
    Username = input("Create username:")
    Password = input("Create password:")
    Password1 = input("Comfirm password:")
    
    if  Password1 != Password:
        print("Passwords don't match, please try again")
        register()
    else:
        if len(Password)<8:
            print("Your password should be at least 8 digits, please enter aonther password")
            register()
        elif Username in userNameList:
            print("Username exists")
            register()
        else: 
            createNewUserQuery = "INSERT INTO uniproject.professor (professor_id, first_name, last_name, username, password) VALUES({0},'{1}','{2}','{3}','{4}');"
            createNewUserQuery = createNewUserQuery.format(max(userIdList)+1,'aa','bb',Username,Password)
            mycursor = cnx.cursor()
            mycursor.execute(createNewUserQuery)
            cnx.commit()
            print("Success!")
            

def access():

    Username = input("Enter your username:")
    Password = input("Enter your password:") 
    
    if  len(Username)>1  and len(Password)>1:
        mycursor = cnx.cursor()
        mycursor.execute("select username , password from uniproject.professor")
        myresult = mycursor.fetchall()
        loginSuccess = False
        for row in myresult:
            if(row[0] == Username and row[1] == Password):
                print("Login success")
                print("Hi,", Username)     
                loginSuccess = True
        if(loginSuccess == False):
            print("Password or Username incorrect")
        
    else:
        print("Please enter a value")
        
            
def home(option=None):
    option = input("Login | Signup:")
    if option.lower() == "login":
        access()
    elif option.lower() == "signup":
        register()
    else:
        print("Please enter an option")
home()

        


def firstPage(allMenu):
 
    for row in allMenu:
        print(row)
   
    userInput = input('please enter your option:')
   
    return userInput
   
   

   
menuIdQuery = "select * from uniproject.menu"
cursor = cnx.cursor()
cursor.execute(menuIdQuery)
    # get all records
allMenuInfo = cursor.fetchall()   
menuIdList = []
menuOption = []
menuAcronym = []
for row in allMenuInfo:
    menuIdList.append(row[0])
    menuAcronym.append(row[2])
    menuOption.append(str(row[0])+'. ' + row[1])
    
   
userInput1 = ''  
while (not userInput1.isnumeric())  or (int(userInput1) not in menuIdList):
    if userInput1!='':
        print('Invaild option')
    userInput1 = firstPage(menuOption)

inputIndex = menuIdList.index(int(userInput1))
if menuAcronym[inputIndex] == ATTANDANCE:
   #do userInput 1 stuff
   print('userInput 1 has been called')
   
elif menuAcronym[inputIndex] == REVIEW_CHART:
   #do userInput 2 stuff
   print('userInput 2 has been called')
   
elif menuAcronym[inputIndex] == S_COURSE_SCORE:
   #do userInput 3 stuff
   print('userInput 3 has been called')
 
   
   
   
   
cnx.close()




