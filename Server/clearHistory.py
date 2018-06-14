import sys
import MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="", db="aplicatiebd")
cur=db.cursor()
stringalau="DELETE FROM history WHERE username='"+sys.argv[1]+"'"
cur.execute(stringalau)
db.commit()