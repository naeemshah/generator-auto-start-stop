import sys
import socket
from socket import error as SocketError
import errno
import RPi.GPIO as GPIO
import time



def checkData( data ):
    if(data == str(1)):
       GPIO.setup(18, GPIO.OUT)  # set up pin 17
       GPIO.output(18, 0)  # turn on pin 17
       
    elif(data == str(2)):
        GPIO.setup(18, GPIO.OUT)  # set up pin 17
        GPIO.output(18, 1)  # turn on pin 17
        
    elif(data == str(3)):
        GPIO.setup(23, GPIO.OUT)  # set up pin 18

        
        GPIO.output(23, 0)  # turn on pin 18
        time.sleep(5)
        
        GPIO.output(23, 1)  # turn on pin 18

    else:
        print "No OP";
    return
    


GPIO.setmode(GPIO.BCM) 


TCP_IP = ''
TCP_PORT = 50051
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(100)

while True:
    conn, addr = s.accept()
    print 'Connection address:', addr
    while 1:
        try:
           data = conn.recv(BUFFER_SIZE)
           if data:
             #print "received data:", data
             checkData(data)
             conn.send(data)  # echo
           #conn.close()
        except SocketError as e:
            print 'Connection close to :', addr
            conn.close()
            break;
            if e.errno != errno.ECONNRESET:
               raise # Not error we are looking for
            pass # Handle error here.


#sys.exit()