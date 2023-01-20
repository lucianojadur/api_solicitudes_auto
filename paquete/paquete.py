import requests
import json
from sys import argv

from sys import path
path.insert(1, '../')
from escape_codes import *
from config import *

path.append('../api')
import api


def alta_paquete(solicitud_tipo):
	paquete = api.API(solicitud_tipo)
	try:
		paquete.full_post_sequence()
	except ValueError:
		print("Flujo terminado.")
		return
	except ConnectionError:
		error_connection_msg()
		return
	except RuntimeError:
		return


def main():
	alta_paquete(argv[1])

main()