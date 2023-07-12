from escape_codes import *
from api import api
import config


def alta(request_type, environment):
	req = api.API(request_type, environment)
	try:
		req.full_post_sequence()
	except ValueError:
		print("Flujo terminado.")
		return
	except ConnectionError:
		config.error_connection_msg()
		return
	except RuntimeError as err:
		print(err.args)
		return


