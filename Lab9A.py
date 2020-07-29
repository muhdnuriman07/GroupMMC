import socket;

#Create a socket object
s = socket.sock();
print("Socket created");

#connect to port number
port = 4567;

#bind to the port
s.bind(('',port));
print("Socket bind to %s" %(port));

#Listen to the port
s.listen(5);
print("Socket is listening....");

#create a forever loop to listen
while True:
    #Establish a connect with clieny
    c,addr =  s.accept();
    print("Connection from",addr);