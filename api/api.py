import requests
import json

from escape_codes import *
import config
import certifi

import ssl

class API:

	def __init__(self, solicitud_type, env):
		self.__sol_type__ = solicitud_type 
		self.__env__ = env

	def full_post_sequence(self):
		try:
			#
			#Solicitud
			response = self.post(config.URL_SOLICITUD, 'solicitudes/solicitud'+self.__sol_type__+'.json', "")
			if response.status_code != 200: 
				self.show("Solicitud", response, "ERROR =>")
				return
			
			id_solicitud = str(response.json()['idSolicitud'])
			self.show("Solicitud", response)
			#
			#Cliente
			cliente_response = self.post(config.URL_CLIENTE, config.CLIENTE_PATH, id_solicitud)
			if response.status_code != 200: 
				self.show("Cliente", response, "ERROR =>")
				return
			
			self.show("Cliente", cliente_response)
			#
			#producto
			response = self.post(
				config.entity[self.__sol_type__][1],\
				config.entity[self.__sol_type__][2],\
				id_solicitud)
			if response.status_code != 200: 
				self.show(config.entity[self.__sol_type__][1], response, "ERROR =>")
				return
			
			self.show(config.entity[self.__sol_type__][0], response)

			enviar = self.post(config.URL_ENVIAR, None, id_solicitud)
			self.show("ENVIAR", enviar)
	
		except ValueError:
			raise
		except requests.exceptions.ConnectionError:
			raise ConnectionError
		except RuntimeError as err:
			raise err


	def post(self, entity_url, entity_json_request_file, id):
		entity_url = entity_url.replace("_env_", config.env[self.__env__])
		entity_url = entity_url.replace("_id_", id)

		requests.packages.urllib3.disable_warnings()	# si verify=False

		try:
			entity = open(entity_json_request_file)
			entity_response = requests.post(entity_url, json=json.load(entity), verify=False)#certifi.where())
			entity.close()	
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
		except TypeError:
			entity_response = requests.post(entity_url.replace("_id_", id), verify=False)#certifi.where())

		return entity_response


	def show(self,  entity_name, response, title=""):
		print(f"{title}{entity_name} response status: " + COLOR[response.status_code // 100] + str(response.status_code) + COLOR[0])
		print(response.json())
		print("\n")