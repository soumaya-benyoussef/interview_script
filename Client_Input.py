__author__ = 'Max W.N.'

import sys
from socket import socket
#from Crypto.PublicKey import RSA
import math

ip_add = str(input('Enter IP Address : '))
port = int(input('Enter Port Number : '))
message = str(input('Enter message : '))

sock = socket()
sock.connect((ip_add, port))
#The socket connects to port number 12321
print("Connection successfully established.")
print("Enter a phrase without spaces seperating words for proper results.")
entered = message

#print("Caesar Cipher Encyption:")
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cba=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
caesar=""
x = []
x = message
track = 0
while(track != len(entered)):
    y=0
    while(y != len(abc)):
        if(x[track]==abc[y]):
            #swap=x.replace(x[track],cba[y])
            caesar+=cba[y]
        # elif(x[track]==' '):
        #     caesar+=' '
        #     y=y+1
        y=y+1
    track=track+1

print("Our input after encryption: " + caesar);
packet = caesar.encode("UTF-8")
sock.send(packet)

buff = sock.recv(2048)
item=buff.decode()

print("Output from our decryption server is: " + item)
sock.close()
