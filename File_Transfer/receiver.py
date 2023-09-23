# this is the script to receive the data of the sender
# now we want to make a progress bar, in order to know how much the program is going to take to receve the file
import tqdm # to be able to make a progress bar
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5002))
server.listen()
client, addr = server.accept()# we are not going to use a while, because we want to receive just one client at the time, but if I want multple clients, I need a whlie loop and a thread for each client

file_name = client.recv(1024).decode() # to receive the file_name with a maximun size of 1024 bytes
print(file_name)

file_size = ord(client.recv(1024).decode()) # to receive the info of the file size with a maximun size of 1024 bytes, but how I send a chr() part, then I use ord to get the intger that was a string

print(file_size)

file1 = open(file_name, "wb") # the file in which we are going to save the received file
file_bytes = b"" # we need to append every single byte that we received becauase there is the probablilyty that we received like b"ho" and then b"la" so to keep together the bytes we use this variable

done = False

progress = tqdm.tqdm(unit="B", unit_scale=True, unit_divisor=1000, total=int(file_size)) # to make the progress bar

while not done:
    data = client.recv(1024)
    #print(data)
    if file_bytes[-5:] == b"<END>": # if the final bytes are <END> then finish the writing mode
        done = True
    else:
        file_bytes += data # append to the variable so this is not going to be in a way that there are breaks
        print(data)
    progress.update(1024) # update the progress bar

file1.write(file_bytes)
file1.close()
client.close()
server.close()

