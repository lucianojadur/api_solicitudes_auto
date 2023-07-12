from escape_codes import *
from api import api
import config


def alta(request_type):
	req = api.API(request_type)
	try:
		req.full_post_sequence()
	except ValueError:
		print("Flujo terminado.")
		return
	except ConnectionError as err:
		config.error_connection_msg()
		return
	except RuntimeError as err:
		print(err.args)
		return


