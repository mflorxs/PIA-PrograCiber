import sys 
import socket
import argparse


#Funcion que ahce el escaneo de puertos 
def funScanPurtos(ip,start_port,end_port):
    #Impresion de la ip y el tipo de dato que es 
    print("Ip", ip, type(ip))

    try:
        #Se empieza la iteracion para el escaneo de puertos
        for port in range(start_port , end_port):
            #Se hace el escano con socket
            sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(5)
            #Se optienen y guardann los resultados
            result= sock.connect_ex((ip,port))
            #Impresion de pantalla de los puertos abiertos
            if result == 0:
                print("Puerto {}: \t Abierto: ".format(port))
            
            sock.close()
    #Se hace la excepcion en caso de que ocurra un error a la hora de conectar a socket 
    except socket.error as error:
        print(str(error))
        print("Error conexion")
        sys.exit()
        
#Funcion donde se asignan los valores desde la terminal con arg parse 
def main():
    parser = argparse.ArgumentParser(description="Herramienta de escaneo de puertos")
    #Se solicita la direccion ip de maneara obligatoria
    parser.add_argument("ip", help="Dirección IP objetivo")
    #se soliciat el inicio de rango de puertos, si no se da ningun valor se toma como default el valor 1
    parser.add_argument("--start-port", type=int, default=1, help="Puerto inicial (por defecto: 1)")
    #se solicita el final de rango de puerto, si no se da ningun valor, se toma como default el valor 300
    parser.add_argument("--end-port", type=int, default=300, help="Puerto final (por defecto: 300)")
    
    #Se asigna los nombre de variables a alos argumentos
    args = parser.parse_args()
    ip = args.ip
    start_port = args.start_port
    end_port = args.end_port
    
    #se manda llamar la funcion donde se hara el escaneo de puertos
    funScanPurtos(ip, start_port, end_port)
    
#inciio del script
if __name__ == "__main__":
    #se manda llamar la funcion main para que se pueda brindar los argumentos desde la terminal con argparse
    main()
    
    



        
        
        
