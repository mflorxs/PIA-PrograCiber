#Modulo en donde se hace la encriptacion de los archivos 

from cryptography.fernet import Fernet
import argparse
import base64



#Generador de llave para cifrado
def genwriet():
    key = Fernet.generate_key()
    with open("pass.key","wb") as key_file:
        key_file.write(key)

#lee el contenido de el contenido del archivo que contiene la llave 
def call_key():
    return open("pass.key","rb").read()

def read_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def save_data_to_txt(data, file_name):
    with open(file_name, 'w') as archivo:
        archivo.write(str(data))
            
    print("Archivo guardado")

def encryption_file(file):
    
    #genera el acrhivo para generar llaves de cifrado
    genwriet()

    #cifrado del mensaje almacenado 
    key= call_key()
    file_path = file
    lines = read_file(file_path)

    # Imprime las líneas leídas del archivo
    for line in lines:
        info_file= line.strip()
    
    banner= info_file.encode()
    a = Fernet(key)
    coded_banner = a.encrypt(banner)
    print(coded_banner)
    save_data_to_txt(coded_banner, file_path)
    





    
    