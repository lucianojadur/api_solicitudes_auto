import requests
import json
from sys import argv

from sys import path
path.insert(1, '../')
from escape_codes import *
from config import *


def alta_prestamo(solicitud_tipo):
	try:
		#
		#Solicitud
		solicitud_response = post(f"Solicitud", URL_SOLICITUD, '../solicitudes/solicitud'+solicitud_tipo+'.json', "")
		id_solicitud = str(solicitud_response.json()['idSolicitud'])
		show("Solicitud", solicitud_response)
		#
		#Cliente
		cliente_response = post("Cliente", URL_CLIENTE, '../cliente/cliente.json', id_solicitud)
		show("Cliente", cliente_response)
		#
		#prestamo
		prestamo_response = post("prestamo", URL_PRESTAMO, 'prestamo.json', id_solicitud)
		show("prestamo", prestamo_response)

		enviar = post("Enviar", URL_ENVIAR, None, id_solicitud)
		show("ENVIAR", enviar)

	except ValueError:
		print("Flujo terminado.")
		return

	except requests.exceptions.ConnectionError:
		print(CODE[5] + "Error de conexión con la API. Chequear que esté activa." + CODE[0])
		


def post(entity_name, entity_url, entity_json_request_file, id):
	try:
		entity = open(entity_json_request_file)
		entity_response = requests.post(entity_url.replace("_id_", id), json=json.load(entity))
		entity.close()
	except FileNotFoundError:
		raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
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


def main():
    alta_prestamo(argv[1])

main()

