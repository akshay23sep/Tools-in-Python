#To check the mac address of your device using python:
import uuid
print ("The MAC address in formatted way is : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) 
for ele in range(0,8*6,8)][::-1])) 


