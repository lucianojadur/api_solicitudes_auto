import requests
import json


from escape_codes import *
from strategy import strategy
import config
import traceback
#import certifi




class API:

	def __init__(self, solicitud_type, env):
		self.__sol_type__ = solicitud_type 
		self.__env__ = env
		self.product_factory = {
			"01": strategy.Required,
			"02": strategy.Required,
			"03": strategy.Required,
			"04": strategy.Required,
			"29": strategy.Unrequired,
			"30": strategy.Unrequired,
			"31": strategy.Unrequired,
			"32": strategy.Unrequired,
			"33": strategy.Unrequired,
			"34": strategy.Unrequired,
			"35": strategy.Unrequired,
			"36": strategy.Unrequired,
			"37": strategy.Unrequired,
			"38": strategy.Unrequired,
			"39": strategy.Unrequired,
			"40": strategy.Unrequired,
			"41": strategy.Unrequired,
			"86": strategy.Required
		}

	def alta(self):
		try:
			self.full_post_sequence()
		except ValueError:
			print("Flujo terminado.")
			return
		except ConnectionError:
			config.error_connection_msg()
			#traceback.print_exc()
			return
		except RuntimeError as err:
			print(err.args)
			return


	def full_post_sequence(self):
		type = self.__sol_type__
		if (int(type)  >= 29 and int(type) <= 42): type = '_seguros'
		try:
			#
			#Solicitud
			solicitud = strategy.Solicitud(self.__sol_type__, self.__env__)
			response = solicitud.post(config.URL_SOLICITUD, 'solicitudes/solicitud'+type+'.json', "")
			if response.status_code != 200: 
				self.show("Solicitud", response, "ERROR =>")
				return
			self.show("Solicitud", response)
			
			id_solicitud = str(response.json()['idSolicitud'])

			cliente = strategy.Required(self.__sol_type__, self.__env__, id_solicitud)
			cliente_response = cliente.post(config.URL_CLIENTE, config.CLIENTE_JSON_PATH)
			if response.status_code != 200: 
				self.show("Cliente", response, "ERROR =>")
				return
			self.show("Cliente", cliente_response)
			
			product = self.product_factory[self.__sol_type__](self.__sol_type__, self.__env__, id_solicitud)	# Instancia un Strategy según si hace falta hacer un POST o no
			response = product.post(
				config.entity[self.__sol_type__][config.URL],\
				config.entity[self.__sol_type__][config.JSON_PATH],
				response)
			if response.status_code != 200: 
				self.show(config.entity[self.__sol_type__][config.URL], response, "ERROR =>")
				return			
			self.show(config.entity[self.__sol_type__][config.NAME], response)
			
			enviar = strategy.Required(self.__sol_type__, self.__env__, id_solicitud)
			response = enviar.post(config.URL_ENVIAR, None, response)
			self.show("ENVIAR", response)
	
		except ValueError:
			raise
		except requests.exceptions.ConnectionError:
			config.error_connection_msg()
			#traceback.print_exc()
			return
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
		print(f"{title} {entity_name} response status: " + COLOR[response.status_code // 100] + str(response.status_code) + COLOR[0])
		print(response.json())
		print("\n")