import MySQLdb
import sys

print(sys.argv[1],sys.argv[2],sys.argv[3])
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="aplicatiebd")
cur = db.cursor()
stringalau="INSERT INTO history(username,command,output) VALUES('"+sys.argv[1]+"','"+sys.argv[2]+"','"+sys.argv[3]+"');"
cur.execute(stringalau)
db.commit()