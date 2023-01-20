import requests
import json
from sys import argv

from sys import path
path.insert(1, '../')
from escape_codes import *
from config import *

path.append('../api')
import api


def alta_prestamo(solicitud_tipo):
	prestamo = api.API(solicitud_tipo)
	try:
		prestamo.full_post_sequence()
	except ValueError:
		print("Flujo terminado.")
		return
	except ConnectionError:
		error_connection_msg()
		return
	except RuntimeError:
		return


def main():
    alta_prestamo(argv[1])

main()

