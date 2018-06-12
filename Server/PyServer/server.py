import socket
import sys
import subprocess
from InstagramAPI import InstagramAPI


class SocketHelper:
    s = None
    conn = None
    addr = None
    username = None
    loggedIn = False
    loggedInIG = False
    userInstagram= None

    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((host, port))
        self.s.listen(5)
        self.userInstagram= InstagramAPI("","")

    def s_appept(self):
        self.conn, self.addr = self.s.accept()

    def send_data(self, content):
        self.conn.send(content)

    def read_data(self):
        buf = self.conn.recv(1024)
        return buf

    def close_socket(self):
        self.conn.close()

User=[]
sockethelper = SocketHelper("localhost", 1333)
print("[i] Server open.\n")
while True:
    sockethelper.s_appept()
	
	#User.append(sockethelper)
    print("[+] Socket open.\n")
    recived = sockethelper.read_data()
    print("[m] " + recived)
    arguments = recived.split(" ")
    to_send = recived + "!"
	
    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
	
	
    if arguments[0] == "login":
        flag = subprocess.check_output([sys.executable, "login.py", arguments[1], arguments[2]])
        if flag == '0':
            to_send = "Error with login creditals. Check again your user/password"
        else:
            to_send = "Login sucessfull"
            sockethelper.loggedIn = True
    elif arguments[0] == "register":
        flag = subprocess.check_output([sys.executable, "register.py", arguments[1], arguments[2], arguments[3]])
        print(flag)
        if flag == "True\n":
            to_send = "You have been registered!"
        else:
            to_send = "There is someone called " + arguments[1]

    elif arguments[0]=="web":
        if sockethelper.loggedIn==False:
            to_send="You have to be logged in to use web module."
        else:
            if arguments[1]=="instagram":
                if arguments[2]=="login":
                    sockethelper.userInstagram=InstagramAPI(arguments[3],arguments[4])
                    if(userInstagram.login()):
                        to_send="You`ve logged in through Instagram. Now you can use it as you desire"
                        loggedInIG = True
                    else:
                        to_send="Wrong username/password. try again after you check them again"

                elif arguments[2]=="follow":
                    if sockethelper.loggedInIG == True :
                        returnID = subprocess.check_output( [sys.executable, "getIDbyUsername.py", arguments[3]])
                        sockethelper.userInstagram.follow(returnID)
                elif arguments[2] == "unfollow":
                    if sockethelper.loggedInIG==True:
                        returnID = subprocess.check_output( [sys.executable, "getIDbyUsername.py", arguments[3]])
                        sockethelper.userInstagram.unfollow(returnID)
                elif arguments[2]=="upload":
                    if sockethelper.loggedInIG == True:
                        if arguments[3]=="photo":
                            caption=""
                            for i in arguments[4:]:
                                caption+=str(i)+" "
                            InstagramAPI.uploadPhoto(arguments[4], caption)

	if arguments[0]=="exit" & len(arguments)==1:
		sockethelper.close_socket
		print("[!] Socket closed.\n")
		
	sockethelper.send_data(to_send)

#	copie dupa diploma de bac
#	copie dupa dcert de nastere

# original:	adeverinta medicala de angajare
# original: cazier  judiciar
# copie legalaizata dupa diploma de bac
# 11 iunie ora 3
# regina maria control de medicina muncii <fisa aptitudini>
