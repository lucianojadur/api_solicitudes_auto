import requests
import json

id_solicitud = ""
URL_SOLICITUD       = "http://localhost:28007/apiSolicitudes/solicitud/"
URL_CLIENTE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cliente/"
URL_AUMENTO_LINEA   = "http://localhost:28007/apiSolicitudes/solicitud/_id_/aumentoLinea/"
URL_PAQUETE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/paquete/"
URL_PRESTAMO        = "http://localhost:28007/apiSolicitudes/solicitud/_id_/prestamo/"
URL_CCOMITENTE      = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cuentaComitente/"

URL_ENVIAR			= "http://localhost:28007/apiSolicitudes/solicitud/_id_/enviar/"

SOLICITUD_BODY = {
	"tipoSolicitud": "86",
	"codigoCanal": "O",
	"codigoOficial": "BR4R",
	"codigoSucursal": "04",
	"codigoGestionDocumental": "CRM421905719125653",
	"monto": "100009.99",
	"origen": "6546",
	"motivoRecepcion": "PLD",
	"estado": "02",
	"excepcion": "false"
}

def alta_paquete():
	#
	#Solicitud
	solicitud = open('solicitud02.json')
	solicitud_response = requests.post(URL_SOLICITUD, json=json.load(solicitud))
	solicitud.close()
	if solicitud_response.status_code != 200:
		print("Solicitud response status: " + str(solicitud_response.status_code))
		return
	id_solicitud = str(solicitud_response.json()['idSolicitud'])
	print(solicitud_response.json())
	#
	#Cliente
	cliente = open('cliente.json')
	cliente_response = requests.post(URL_CLIENTE.replace("_id_", id_solicitud), json=json.load(cliente))
	cliente.close()
	print("Cliente response status: " + str(cliente_response.status_code))
	if cliente_response.status_code != 200:
		print(cliente_response.json())
		return 
	#
	#Paquete
	paquete = open('paquete.json')
	paquete_response = requests.post(URL_PAQUETE.replace("_id_", id_solicitud), json=json.load(paquete))
	paquete.close()
	print("Paquete response status: " + str(paquete_response.status_code))
	if paquete_response.status_code != 200:
		print(paquete_response.json())
		return
	enviar = requests.post(URL_ENVIAR.replace("_id_",  id_solicitud))
	print("\nENVIAR: " + str(enviar.status_code))
	print(enviar.json())

alta_paquete()