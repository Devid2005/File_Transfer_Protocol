# this program is to pass files between two system that use socket 
# so this is the sender script, remmember that you are going to send the file in bytes

import os
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # initialiting the socket
client.connect(("localhost", 5002))

# as sender, we know what is the side of the file, so we can send it as as bytes wihout any problem
file1 = open('{path_file}', 'rb') # path_file is the location of the file that you want to send
file_size = int(os.path.getsize("{path_file}")) # but we want to give some information to the receiver of how long it's the size of the file

client.send("received_image.png".encode()) # this is message to client, to inform wich extension is going to recevied

a = chr(file_size) # there is a problem with the encode method with an input of int, so I use the chr() to convert it into a string, indorder to not get any problem with the decode

client.send(a.encode()) # inform to the client which is the size of the file


data = file1.read() # this is going to give you in hexadecimal reading, the codification of the image
client.sendall(data) # how you are the sender, you don't need to specific noting to send, so you can sendall wihout any problem
client.send(b"<END>") # a message to say that you have finish

file1.close()
client.close()

