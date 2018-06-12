# Import socket module
import socket
 
 
def Main():
    host = '127.0.0.1'
 
    port = 6636
 
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 
    s.connect((host,port))
    
    message = "shaurya says geeksforgeeks"
    while True:
        text=raw_input("C>")
        if text=="quit":
            break
        s.send(text.encode('ascii'))
 
        # messaga received from server
        data = s.recv(1024)
        print('Received from the server :',str(data.decode('ascii')))
 
    s.close()
 
if __name__ == '__main__':
    Main()