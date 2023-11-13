import socket
from datetime import datetime
import nmap 



ipportsopen=[]



def scan(addr):
   s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   socket.setdefaulttimeout(1)
   result = s.connect_ex((addr,135))
   if result == 0:
      return 1
   else :
      return 0

def run1():
   for ip in range(st1,en1):
      addr = net2 + str(ip)
      if (scan(addr)):
         
         ipportsopen.append(addr)
         
         
def escanear_puertos(host):
    nm = nmap.PortScanner()
    resultado = nm.scan(host, arguments='-p-')
    
    for puerto in resultado['scan'][host]['tcp']:
        estado = resultado['scan'][host]['tcp'][puerto]['state']
        servicio = resultado['scan'][host]['tcp'][puerto]['name']
        version = resultado['scan'][host]['tcp'][puerto]['version']
        
        print(f"Puerto {puerto} - Estado: {estado} - Servicio: {servicio} - Versión: {version}")


# Se agrega la dirección IP del dispositivo gateway
net = input("Ingrese la direccion IP del gateway: ")
net1 = net.split('.')
a = '.'

# Se define el rango de direcciones IP que se desea analizar, dependera de la mascara de la red en estudio
net2 = net1[0] + a + net1[1] + a + net1[2] + a
st1 = int(input("Ingrese IP inicial: "))
en1 = int(input("Ingrese IP final: "))
en1 = en1 + 1
t1 = datetime.now()

run1()
print(ipportsopen)

for i in ipportsopen:
       escanear_puertos(i)
       

t2 = datetime.now()
total = t2 - t1