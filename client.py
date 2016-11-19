import sys
import socket



# class client :
#     def __int__(self):
#         self.TCP_IP = '127.0.0.1'
#         self.TCP_PORT = 5005
#         self.BUFFER_SIZE = 1024

#     def printOptions(self):
       # while True:
            #print "1 : For start server"
            #print "2 : Quit"
            #inp = raw_input("Please enter a number")
            
            # if inp == 1:
            #    print inp
            # elif inp == 2:
            #    print inp
            # else:
            #    print "fuck you";
        



# if __name__ == "__main__":
#    c = client()
#    c.printOptions



class Client:


   
   empCount = 0
   TCP_IP = '192.168.10.100'
   TCP_PORT = 50051
   BUFFER_SIZE = 1024
   soc = None

   def __int__(self):
    self.hello = 0;
        
       
        

   
   
   def display(self):
      while True:
            print "1 : For start server"
            print "2 : Quit"
            inp = input("Please enter a number: ")
            
            if inp == 1:
               self.connect();
               
               #data = s.recv(BUFFER_SIZE)
            elif inp == 2:
                while 1:
                   inp2 = input("Please enter a number to Sent to server : ")
                   if(inp2 == 1 or inp2 == 2 or inp2 == 3):
                     self.soc.send(str(inp2))
                   else: 
                    break;
               
            elif inp == 3:
                self.closeConnection();
            elif inp == 4:
                break;

            else:
                print "Not Valid";

   def closeConnection(self):
        self.soc.close()


   def connect(self):
        if(self.soc == None):
           self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           self.soc.connect((self.TCP_IP, self.TCP_PORT))
        

  


emp1 = Client()

emp1.display()















# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((TCP_IP, TCP_PORT))

# # Commenting out the following to prove the recv() call on the other
# #end returns with nothing instead of blocking indefinitely.  If I
# #type the rest of this at the REPL the server behaves correctly,
# #ie, the recv call blocks forever until socket.send("bla") from client.

# s.send(MESSAGE) 
# data = s.recv(BUFFER_SIZE)
# s.close()
# print "received data:", data
# sys.exit()