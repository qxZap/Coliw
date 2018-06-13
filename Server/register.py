import MySQLdb
import sys

def functionRegister(userName,Password,Email):
    db = MySQLdb.connect(host="localhost", user="root", passwd="", db="aplicatiebd")
    cur = db.cursor()
    stringalau="SELECT id FROM USERS WHERE username ='"+userName+"'"
    cur.execute(stringalau)
    if len(cur.fetchall())>0:
		return False
    else:
		stringalau="INSERT INTO users(username,password,email) VALUES('"+userName+"','"+Password+"','"+Email+"');"
		cur.execute(stringalau)
		db.commit()
		return True


print(functionRegister(sys.argv[1],sys.argv[2],sys.argv[3]))