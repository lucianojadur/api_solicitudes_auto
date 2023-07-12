import requests
import json

from escape_codes import *
import config


class API:

	def __init__(self, solicitud_type, env):
		self.__sol_type__ = solicitud_type 
		self.__env__ = env

	def full_post_sequence(self):
		try:
			#
			#Solicitud
			solicitud_response = self.post(config.URL_SOLICITUD, 'solicitudes/solicitud'+self.__sol_type__+'.json', "")
			if solicitud_response != 200: 
				self.show("Solicitud", solicitud_response, "ERROR =>")
				return
			
			id_solicitud = str(solicitud_response.json()['idSolicitud'])
			self.show("Solicitud", solicitud_response)
			#
			#Cliente
			cliente_response = self.post(config.URL_CLIENTE, config.CLIENTE_PATH, id_solicitud)
			self.show("Cliente", cliente_response)
			#
			#producto
			entity_response = self.post(
				config.entity[self.__sol_type__][0],\
				config.entity[self.__sol_type__][1],\
				config.entity[self.__sol_type__][2],\
				id_solicitud)
			self.show(config.entity[self.__sol_type__][0], entity_response)

			enviar = self.post(config.URL_ENVIAR, None, id_solicitud, self.__env__)
			self.show("ENVIAR", enviar)
	
		except ValueError:
			raise
		except requests.exceptions.ConnectionError:
			raise ConnectionError
		except RuntimeError as err:
			raise err


	def post(self, entity_url, entity_json_request_file, id):
		try:
			entity = open(entity_json_request_file)
			entity_url = entity_url.replace("_env_", config.env[self.__env__])
			entity_url = entity_url.replace("_id_", id)
			
			entity_response = requests.post(entity_url, json=json.load(entity), verify=False)
			entity.close()
			
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
		except TypeError:
			entity_response = requests.post(entity_url.replace("_id_", id), verify=False)
		
	#	if entity_response.status_code != 200:
	#		print("\n----------- Error - api.post() - Linea 57:\n")
	#		self.show(entity_name, entity_response, "ERROR => ")
	#		#raise ValueError

		return entity_response


	def show(self,  entity_name, response, title=""):
		print(f"{title}{entity_name} response status: " + COLOR[response.status_code // 100] + str(response.status_code) + COLOR[0])
		print(response.json())
		print("\n")