import smtplib
import os 
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import datetime
import socket
from datetime import datetime

def funSendReportEmail(remitente,destinatario,asunto,archEncri):
    
    #Obtiene tanto la fecha/hora actual y el nombre del equipo
    fecha_hora_actual = datetime.now()
    nombre_equipo = socket.gethostname()
    
    #se determina el asunto, remitennte y destinatario para el envio del correo
    msg= MIMEMultipart()
    msg['Subject']=asunto
    msg['From']=remitente
    msg['To']=destinatario

    #Se crea el html para dar formato al contenido del correo
    html = """
        <html>
        <body>
            <H1> Reporte de escaneo </H1>
            <a>Hola buen dia, por este medio le hago llegar el reporte de escaneo </a><br><br>
            <a>Fecha: """+str(fecha_hora_actual)+"""</a> <br><br>
            <a>Equipo de escnaneo: """+str(nombre_equipo)+"""</a> <br><br>
            <a>Saludos cordiales </a><br><br>
        </body>
        </html>
        """
    #Se agrega al contenido del mensaje del corroe
    msg.attach(MIMEText(html, 'html'))

    #Se toma el archivo adjunto a enviar, se toma ejemplo con una imagen png
    image_path = archEncri
    #Se abre el archivo para poderlo manipular en el script
    
    with open(image_path, "rb") as image_file:
        #Se agrega al contenido del correo
        image = MIMEImage(image_file.read(), name="imagen.png")
        msg.attach(image)

    #se empieza a hacer la conexion con el 
    conn = smtplib.SMTP('smtp.gmail.com', 587)
    conn.ehlo()
    

    conn.starttls()
    conn.login('senacastillo3@gmail.com','jgyw vibz epwn eeiz')
    #Se hace el envio de informacion
    conn.sendmail(remitente,destinatario,msg.as_string(),)
    #Se cierra la conexion
    conn.quit