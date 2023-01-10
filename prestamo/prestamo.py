import requests
import json
from sys import argv

from sys import path
path.insert(1, '../')
from escape_codes import *
from config import *

path.append('../api')
import api as API


def alta_prestamo(solicitud_tipo):
	try:
		#
		#Solicitud
		solicitud_response = API.post(f"Solicitud", URL_SOLICITUD, '../solicitudes/solicitud'+solicitud_tipo+'.json', "")
		id_solicitud = str(solicitud_response.json()['idSolicitud'])
		API.show("Solicitud", solicitud_response)
		#
		#Cliente
		cliente_response = API.post("Cliente", URL_CLIENTE, '../cliente/cliente.json', id_solicitud)
		API.show("Cliente", cliente_response)
		#
		#prestamo
		prestamo_response = API.post("prestamo", URL_PRESTAMO, 'prestamo.json', id_solicitud)
		API.show("prestamo", prestamo_response)

		enviar = API.post("Enviar", URL_ENVIAR, None, id_solicitud)
		API.show("ENVIAR", enviar)

	except ValueError:
		print("Flujo terminado.")
		return

	except requests.exceptions.ConnectionError:
		API.error_connection_msg()		



#def main():
#    alta_prestamo(argv[1])

#main()

