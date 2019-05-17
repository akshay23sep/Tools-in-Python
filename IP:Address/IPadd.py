#In order to get IP address of your device in Python
#Just install the library socket
#pip install socket
#Importing the library
import socket
hname = socket.gethname()
IPAddr = socket.gethostbyname(hname)
print("The name of your device is: :" + hname)
print("The IP Address of your device is:" + IPAddr)
