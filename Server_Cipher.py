__author__ = 'Max W.N.'


import math
from socket import socket

ip_add = str(input('Enter IP Address : '))
port = int(input('Enter Port Number : '))

listening = socket()
listening.bind((ip_add, port))
listening.listen(5) #the argument is the amount of room our backlog has for cluttered requests!
print("Establishing connection.")

(conn, address) = listening.accept()
print("Connection established.", conn, address)
#space will be used to call functions!

buffer = conn.recv(2048)

print("Received: ", buffer)

decoded = buffer.decode()

print("Decoded: " + decoded)

#Caesar Cipher Decryption Method:######################################################################################
abc=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
cba=['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
caesar=""
x = []
x = decoded
track = 0
while(track != len(decoded)):
    y=0
    while(y != len(abc)):
        if(x[track]==cba[y]):
            #swap=x.replace(x[track],cba[y])
            caesar+=abc[y]
        # elif(x[track]==' '):
        #     caesar+=' '
        #     y=y+1
        y=y+1
    track=track+1


output=caesar

conn.send(output.encode())
conn.close()
listening.close()   
