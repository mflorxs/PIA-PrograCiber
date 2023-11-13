#Script que envia los correos electronicos
'''
El script esta dividido en dos partes, este script es el script principal en dode 
va a llamar el modulo moduloemail creado por nostros, este ultimo tiene las biblotecas
e instrucciones paar enviar el correo.
'''
#Se importa el modulo para el envio del correo 
from moduloemail import funSendReportEmail
from datetime import datetime 

#Funcion que prepara el envio del correo
def funPreSendEmail(archivoresult):
    #Variable donde se saca la fecha y hora actual 
    fecha_hora_actual = datetime.now()

    #se definenen los parametros para la funcion que se encuentar en el modulo
    remitente= "senacastillo3@gmail.com"#correo de quein va enviar 
    destinatario= "antonio.senacst@uanl.edu.mx"#correo de quien recibe 
    asunto="Escaneo "+str(fecha_hora_actual)#Asunto del correo
    archEncri=archivoresult#Archivo en donde se alamacena la informacion 

    #Se manda a llamar la funcion del modulo que envia el correo 
    funSendReportEmail(remitente,destinatario,asunto,archEncri)
    

