
#Lab 9B and 9C
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
                              
