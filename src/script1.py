import base64
import requests
import json
from datetime import datetime

#Función para buscar recursivamente herramientas que consideran el destino malicioso o sospechoso, y regresa una lista de herramientas
def buscar_mali(dicc):
	lista = []
	#Buscamos los resultados del analisis de cada herramienta
	for c, v in dicc.items():
		if isinstance(v, dict):
			#Si la herramienta encuentra el destino sospechoso o malicioso, se guarda su nombre en una lista
			if v["category"] == 'malicious' or v["category"] == 'suspicious':
				tool = v["engine_name"] + " : " + v["result"]
				lista.append(tool)
	return (str(lista))

#Recibimos el URL y se encripta en base64
url = input ("URL: ")
url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")

#Obtenemos la Apikey del archivo .key
with open ('../Api Keys/VirusTotal.key', 'r') as key:
	apikey = key.read()

#Se crean las variables necesarias y se hace un request a la API, guardamos la respuesta en una variable
url_api = "https://www.virustotal.com/api/v3/urls/" + url_id
headers = {
    "accept": "application/json",
    "x-apikey": apikey
}
respuesta = requests.get(url_api, headers=headers)

#Se crea una excepción en caso de que el request devuelva un error
if respuesta.status_code != 200:
	print("Introdujiste una URL invalida")
	exit()

#Convertimos la respuesta de una response a un diccionario
resp_json = respuesta.json()
#Se navega hasta el diccionario que contiene los resultados del análisis y se guarda en una variable
analisis = resp_json["data"]["attributes"]["last_analysis_stats"]

#Creamos el texto que aparecera en el archivo de Consulta con todos los resultados
inofensivo = f"{analisis['harmless']} herramientas encontraron el destino inofensivo \n"
malicioso = f"{analisis['malicious']} herramientas encontraron el destino malicioso \n"
sospechoso = f"{analisis['suspicious']} herramientas encontraron el destino sospechoso \n"
undet = f"{analisis['undetected']} herramientas no detectaron el destino \n"
msg = (
    f"El análisis con la API de VirusTotal arrojó las siguientes estadísticas sobre el destino {url} \n"
    f"De 90 análisis con diferentes herramientas se obtuvieron los resultados: \n"
    f"{inofensivo}{malicioso}{sospechoso}{undet}"
)
#Se crea una variable vacía
msg1 = ''
#Para cada herramienta que encuentre el destino malicioso o sospechoso, se llama a la función que agregara su nombre en una lista y la regresa
if analisis['malicious'] > 0 or analisis['suspicious'] > 0:
	mali_tools = resp_json["data"]["attributes"]["last_analysis_results"]
	msg1 = "\nLa siguientes herramientas encontraron el destino malicioso o sospechoso: \n" + buscar_mali(mali_tools)

#Creamos una variable con el tiempo actual 
tiempo = datetime.now()
#Le damos el formato requerido 
fh = tiempo.strftime("%d-%m-%Y_%H-%M-%S")
#Creamos el archivo del reporte y agregamos el texto del analisis
with open("consulta_" + fh + ".txt", 'w') as file:
	file.write(msg)
	file.write(msg1)
with open ('reporte.txt', 'w') as file:
	file.write(respuesta.text)