#Lab 9A
# First import the socket library
import socket;
import sys

#Create a socket object
s = socket.socket();
print("Socket created");

#Connect to port number
port = 4567;

# Bind to the port
s.bind(('',port));
print("Socket bind to %s" %(port));

# Listen to the port
s.listen(5);
print("Socket is listening...");

# Create a forever loop to listen

while True:
 #Establish connection with client
 c, addr = s.accept();
 print("Connection from",addr);

#================================================================================================================================== 

#Lab 9B
try:
 #Where AF_INET specify IPv4
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM);
 print("Socket created succefully")
 
 except socket.error as err:
  print("Socket creation failed with error %s"%(err)):
   
#Default web port
port=80;
try:
 host_ip = socket.gethostbyname("www.google.com")
 except socket.gaierror:
  print("There is a problem resolving the host")
  sys.exit();
  
 #connect to the web Server
 s.connect((host_ip,port));
 print("Successfully connected to the website given %s:%s"%(host_ip,port));
                              
