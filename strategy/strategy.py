import requests
import json
#import traceback
from abc import abstractmethod 

import sys
sys.path.append("..")

from escape_codes import *
import config

PROXIES = {'https': 'http://localhost:28007'}

class Strategy:

	def __init__(self, type, env) -> None:
		pass

	@abstractmethod
	def post(self):
		pass
		

class Solicitud(Strategy):
	def __init__(self, type, env):
		self.__type__ = type
		self.__env__ = env

	def post(self, entity_url, entity_json_request_file, id, prev_response=None):
		url = entity_url.replace("_env_", config.env[self.__env__])
		url = url.replace("_id_", id)
		
		if self.__env__ == "local":
			url = url.replace("https", "http")				
		
		requests.packages.urllib3.disable_warnings()	# si verify=False
		if self.__env__ == "local": verif = None
		else: verif = False
		
		try:
			entity = open(entity_json_request_file)
			response = requests.post(url, json=json.load(entity), verify=False)#certifi.where())
			entity.close()	
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
			
		return response
	

class Required(Strategy):

	def __init__(self, type, env, id):
		self.__type__ = type
		self.__env__ = env
		self.__id__ = id

	def post(self, entity_url,  entity_json_request_file, prev_response=None):
		url = entity_url.replace("_env_", config.env[self.__env__])
		url = url.replace("_id_", self.__id__)

		if self.__env__ == "local":
			url = url.replace("https", "http")
		
		print(f"CLIENTE URL: {url}")
		requests.packages.urllib3.disable_warnings()	# si verify=False

		try:
			entity = open(entity_json_request_file)
			response = requests.post(url, json=json.load(entity), verify=False)#certifi.where())
			entity.close()
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")
		except TypeError:
			response = requests.post(url, verify=False)#certifi.where())

		return response


class Unrequired(Strategy):

	def post(self, entity_url,  entity_json_request_file, prev_response):
		return prev_response