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
 
#End of function
parser = argparse.ArgumentParser(description="Learn to connect to a website with port number");
parser.add_argument("-H", "--host", required=True, help="specify the hostname or website name");
parser.add_argument("-p", "--port", type=int, default=80, help="specify the port number eg. 80 for website");

args = parser.parse_args();
ploadconnect(args.host,args.port);

                              
