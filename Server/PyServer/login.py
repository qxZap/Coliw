import MySQLdb
import sys



def functionLogin(userName,Password):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="aplicatiebd")
    cur = db.cursor()
    stringalau="SELECT password FROM USERS WHERE username ='"+userName+"'"
    cur.execute(stringalau)
    if Password==cur.fetchall()[0][0]:
        return True
    else:
        return False



if(functionLogin(sys.argv[1],sys.argv[2])):
    print('1')
else:
    print('0')
