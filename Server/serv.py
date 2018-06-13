import socket
import sys
from thread import start_new_thread
from InstagramAPI import InstagramAPI
import subprocess
import flickrapi

HOST = '' 
PORT = 6636 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print("Could not create socket. Error Code: ", str(msg[0]), "Error: ", msg[1])
    sys.exit(0)

print("[+] Socket Created")

try:
    s.bind((HOST, PORT))
    print("[-] Socket Bound to port " + str(PORT))
except socket.error, msg:
    print("Bind Failed. Error Code: {} Error: {}".format(str(msg[0]), msg[1]))
    sys.exit()

s.listen(10)
print("[!] Listening...")


def client_thread(conn,addr):
    loggedIn = False
    loggedInIG = False
    userInstagram= None
    while True:
        try:
            data = conn.recv(1024)
        except Exception as disconnected:
            print("[-] Disconnected "+addr[0]+":"+str(addr[1]))
            q=disconnected
            break
        if not data:
            break
        arguments = data.split(" ")
        
        if arguments[0] == "login":
            flag = subprocess.check_output([sys.executable, "login.py", arguments[1], arguments[2]])
            if flag == '0':
                to_send = "Error with login creditals. Check again your user/password"
            else:
                to_send = "Login sucessfull"
                loggedIn = True
        elif arguments[0] == "register":
            flag = subprocess.check_output([sys.executable, "register.py", arguments[1], arguments[2], arguments[3]])
            if flag == "True\n":
                to_send = "You have been registered!"
            else:
                to_send = "There is someone called " + arguments[1]
                
        elif arguments[0]=="web":
            if loggedIn==False:
                to_send="You have to be logged in to use web module."
            else:
                if len(arguments)>1:
                    if arguments[1]=="instagram":
                        if arguments[2]=="login":
                            userInstagram=InstagramAPI(arguments[3],arguments[4])
                            if(userInstagram.login()):
                                to_send="You`ve logged in through Instagram. Now you can use it as you desire"
                                loggedInIG = True
                            else:
                                to_send="Wrong username/password. try again after you check them again"

                        elif arguments[2]=="follow":
                            if loggedInIG == True :
                                returnID = subprocess.check_output( [sys.executable, "getIDbyUsername.py", arguments[3]])
                                if returnID[len(returnID)-1]=='"':
                                    returnID=returnID[:-1]
                                userInstagram.follow(returnID)
                        elif arguments[2] == "unfollow":
                            if loggedInIG==True:
                                returnID = subprocess.check_output( [sys.executable, "getIDbyUsername.py", arguments[3]])
                                if returnID[len(returnID)-1]=='"':
                                    returnID=returnID[:-1]
                                userInstagram.unfollow(returnID)
                        elif arguments[2]=="upload":
                            if loggedInIG == True:
                                if arguments[3]=="photo":
                                    caption=""
                                    for i in arguments[4:]:
                                        caption+=str(i)+" "
                                    uploadPhoto(arguments[4], caption)
                    elif arguments[1] == "flickr":
                        continueT=True
                        index_to_start=0
                        number_of_photos=0
                        #web flickr
                        if len(arguments)==2:
                            to_send="no arguments given!"
                        #web flickr <tag>
                        elif len(arguments)==3:
                            if arguments[2]=='-h':
                                to_send="\nFlickr api\nSyntax: web flickr <keyword> <options>\n\n\t-i start index ( 0 as default )\n\t-n number of photos ( 1 as default )"
                                continueT=False
                            else:
                                index_to_start=1
                                number_of_photos=1
                            
                        elif len(arguments)==5:
                            if arguments[3]=='-i':
                                if arguments[4].isdigit():
                                    index_to_start=int(arguments[4])
                                else:
                                    continueT=False
                                    to_send=argument[4]+" is not a number"
                        
                            elif arguments[3]=='-n':
                                if arguments[4].isdigit():
                                    number_of_photos=int(arguments[4])
                                else:
                                    continueT=False
                                    to_send=argument[4]+" is not a number"
                        
                        
                            
                        elif len(arguments)==6:
                            if arguments[3]=='-in':
                                
                                if arguments[4].isdigit():
                                    index_to_start=int(arguments[4])
                                else:
                                    continueT=False
                                    to_send=arguments[4]+" is not a number"
                                     
                                if arguments[5].isdigit():
                                    number_of_photos=int(arguments[5])
                                else:
                                    continueT=False
                                    to_send=arguments[5]+" is not a number"
                                    
                            elif arguments[3]=='-ni':
                                    
                                if arguments[4].isdigit():
                                    number_of_photos=int(arguments[4])
                                else:
                                    continueT=False
                                    to_send=arguments[4]+" is not a number"
                                        
                                if arguments[5].isdigit():
                                    index_to_start=int(arguments[5])
                                else:
                                    continueT=False
                                    to_send=arguments[5]+" is not a number"                                    
                        elif len(arguments)==7:
                            if arguments[3]=='-i' and arguments[5]=='-n':
                                if arguments[4].isdigit():
                                    if arguments[6].isdigit():
                                        index_to_start=int(arguments[4])
                                        number_of_photos=int(arguments[6])
                                    else:
                                        continueT=False
                                        to_send=arguments[6]+" is not a number"
                                else:
                                    continueT=False
                                    to_send=arguments[4]+" is not a number"
                            
                            elif arguments[3]=='-n' and arguments[5]=='-i':
                                if arguments[4].isdigit():
                                    if arguments[6].isdigit():
                                        number_of_photos=int(arguments[4])
                                        index_to_start=int(arguments[6])
                                    else:
                                        continueT=False
                                        to_send=arguments[6]+" is not a number"
                                else:
                                    continueT=False
                                    to_send=arguments[4]+" is not a number"
                            elif arguments[3]==arguments[5]:
                                continueT=False
                                to_send="3rd and 5th argument cannot be even"
                            else:
                                continueT=False
                                to_send="Wrong syntax, expected -i or -n on the 3rd or 5th"
                        
                        
                        else:
                            to_send="Too many arguments given/wrong syntax"
                            continueT=False
                        if continueT:
                            #to_send="Right syntax/ you wanna search "+arguments[2]+" index="+str(index_to_start)+" no="+str(number_of_photos)
                            startUP=0
                            startDOWN=0
                            if number_of_photos==0:
                                number_of_photos=1
                            if number_of_photos==1 and index_to_start==1:
                                startUP=0
                                startDOWN=1
                            elif index_to_start==0 and number_of_photos>1:
                                startUP=0
                                startDOWN=number_of_photos
                            elif index_to_start>1 and number_of_photos==1:
                                startUP=index_to_start
                                startDOWN=index_to_start+1
                            elif index_to_start>1 and number_of_photos>1:
                                startUP=index_to_start
                                startDOWN=startUP+number_of_photos
                            elif index_to_start==1 and number_of_photos>1:
                                startUP=index_to_start
                                startDOWN=number_of_photos+1
                            elif index_to_start==0 and number_of_photos==1:
                                startUP=0
                                startDOWN=1
                                
                            
                                
                            
                            
                                
                            flickr = flickrapi.FlickrAPI('e57cfa37f00d7a9a5d7fac7e37ebcbb5', '00751b0c7b65ba7a',format='parsed-json')
                            extras = 'url_sq,url_t,url_s,url_q,url_m,url_n,url_z,url_c,url_l,url_o'
                            links = ""
                            cats = flickr.photos.search(text=arguments[2], per_page=startDOWN+startUP, extras=extras)
                                
                            for i in range(startUP, startDOWN):
                                photos = cats['photos']['photo'][i]['url_m']
                                links =links+photos + '\n'
                            links=links[:-1] 
                            to_send=links
                            
                    else:
                        to_send="unknown web command"
                else:
                    to_send="too few arguments known"
        else:
            to_send=arguments[0]+" is not recognized"
            
        reply = to_send
        conn.send(reply)
    conn.close()

while True:
    conn, addr = s.accept()
    print("[+] Connected to " + addr[0] + ":" + str(addr[1]))

    start_new_thread(client_thread, (conn,addr))

s.close()