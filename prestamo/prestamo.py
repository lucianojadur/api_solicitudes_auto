
from api import api
import config


def alta(solicitud_tipo):
	prestamo = api.API(solicitud_tipo)
	try:
		prestamo.full_post_sequence()
	except ValueError:
		print("Flujo terminado.")
		return
	except ConnectionError:
		config.error_connection_msg()
		return
	except RuntimeError as err:
		print(err.args)
		return




