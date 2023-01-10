import requests
import json

from escape_codes import *

id_solicitud = ""
URL_SOLICITUD       = "http://localhost:28007/apiSolicitudes/solicitud/"
URL_CLIENTE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cliente/"
URL_AUMENTO_LINEA   = "http://localhost:28007/apiSolicitudes/solicitud/_id_/aumentoLinea/"
URL_PAQUETE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/paquete/"
URL_PRESTAMO        = "http://localhost:28007/apiSolicitudes/solicitud/_id_/prestamo/"
URL_CCOMITENTE      = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cuentaComitente/"

URL_ENVIAR			= "http://localhost:28007/apiSolicitudes/solicitud/_id_/enviar/"


def alta_paquete():
	try:
		#
		#Solicitud
		solicitud_response = post("Solicitud", URL_SOLICITUD, 'solicitud02.json', "")
		id_solicitud = str(solicitud_response.json()['idSolicitud'])
		show("Solicitud", solicitud_response)
		#
		#Cliente
		cliente_response = post("Cliente", URL_CLIENTE, 'cliente.json', id_solicitud)
		show("Cliente", cliente_response)
		#
		#Paquete
		paquete_response = post("Paquete", URL_PAQUETE, 'paquete.json', id_solicitud)
		show("Paquete", paquete_response)

		enviar = post("Enviar", URL_ENVIAR, None, id_solicitud)
		show("ENVIAR", enviar)

	except ValueError:
		print("Flujo terminado.")
		return

	except requests.exceptions.ConnectionError:
		print(CODE[5] + "Error de conexión con la API. Chequear que esté activa." + CODE[0])
		


def post(entity_name, entity_url, entity_json_request, id):
	try:
		entity = open(entity_json_request)
		entity_response = requests.post(entity_url.replace("_id_", id), json=json.load(entity))
		entity.close()
	except FileNotFoundError:
		raise RuntimeError(f"Archivo {entity_json_request} inválido o no existe")
	except TypeError:
		entity_response = requests.post(entity_url.replace("_id_", id))
	
	if entity_response.status_code != 200:
		show("ERROR => " + entity_name, entity_response)
		raise ValueError

	return entity_response


def show(entity_name, response):
	if entity_name != "Solicitud": print(f"{entity_name} response status: " + CODE[response.status_code // 100] + str(response.status_code) + CODE[0])
	print(response.json())
	print("\n")


alta_paquete()


