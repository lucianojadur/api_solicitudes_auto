import requests
import json

from sys import path
path.append('../setup')
from escape_codes import *
from config import *


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