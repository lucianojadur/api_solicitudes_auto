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

	def format_url(self, entity_url, id):
		url = entity_url.replace("_env_", config.env[self.__env__])
		url = url.replace("_id_", id)
		if self.__env__ == "local":
			url = url.replace("https", "http")		
		return url


class Solicitud(Strategy):
	def __init__(self, type, env):
		self.__type__ = type
		self.__env__ = env

	def post(self, entity_url, json_path, id, prev_response=None):
		url = self.format_url(entity_url, id)
		
		if self.__env__ == "local":
			url = url.replace("https", "http")				
		
		requests.packages.urllib3.disable_warnings()	# si verify=False
		if self.__env__ == "local": verif = None
		else: verif = False
		
		try:
			entity = open(json_path)
			response = requests.post(url, json=json.load(entity), verify=False)#certifi.where())
			entity.close()	
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {json_path} inválido o no existe")
			
		return response
	


class Required(Strategy):

	def __init__(self, type, env, id):
		self.__type__ = type
		self.__env__ = env
		self.__id__ = id


	def post(self, entity_url,  json_path, prev_response=None):
		url = self.format_url(entity_url, self.__id__)

		if self.__env__ == "local":
			url = url.replace("https", "http")
		
		requests.packages.urllib3.disable_warnings()	# si verify=False
		try:
			entity = open(json_path)
			response = requests.post(url, json=json.load(entity), verify=False)#certifi.where())
			entity.close()
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {json_path} inválido o no existe")
		except TypeError as e:
			response = requests.post(url, verify=False)#certifi.where())

		return response


class Unrequired(Strategy):

	def __init__(self, type, env, id):
		self.__type__ = type, 
		self.__env__ = env
		self.__id__ = id

	def post(self, entity_url,  json_path, prev_response):
		return prev_response