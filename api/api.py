import requests
import json

from sys import path
path.append('../setup')
from escape_codes import *
import config


class API:

	def __init__(self, solicitud_type):
		self.__sol_type__ = solicitud_type 


	def full_post_sequence(self):
		try:
			#
			#Solicitud
			solicitud_response = self.post(f"Solicitud", config.URL_SOLICITUD, '../solicitudes/solicitud'+self.__sol_type__+'.json', "")
			id_solicitud = str(solicitud_response.json()['idSolicitud'])
			self.show("Solicitud", solicitud_response)
			#
			#Cliente
			cliente_response = self.post("Cliente", config.URL_CLIENTE, config.CLIENTE_PATH, id_solicitud)
			self.show("Cliente", cliente_response)
			#
			#prestamo
			entity_response = self.post(
				config.entity[self.__sol_type__][0],\
				config.entity[self.__sol_type__][1],\
				config.entity[self.__sol_type__][2],\
				id_solicitud)
			self.show("prestamo", entity_response)

			enviar = self.post("Enviar", config.URL_ENVIAR, None, id_solicitud)
			self.show("ENVIAR", enviar)

		except ValueError:
			raise
		except requests.exceptions.ConnectionError:
			raise ConnectionError
		except RuntimeError:
			raise


	def post(self, entity_name, entity_url, entity_json_request_file, id):
		try:
			entity = open(entity_json_request_file)
			entity_response = requests.post(entity_url.replace("_id_", id), json=json.load(entity))
			entity.close()
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
		except TypeError:
			entity_response = requests.post(entity_url.replace("_id_", id))
		
		if entity_response.status_code != 200:
			self.show("ERROR => " + entity_name, entity_response)
			raise ValueError

		return entity_response


	def show(self, entity_name, response):
		if entity_name != "Solicitud": print(f"{entity_name} response status: " + CODE[response.status_code // 100] + str(response.status_code) + CODE[0])
		print(response.json())
		print("\n")