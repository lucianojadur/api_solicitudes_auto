from strategy import strategy

class Solicitud(strategy.Strategy):
	def __init__(self, type, env):
		self.__type__ = type
		self.__env__ = env

	def post(self, entity_url, entity_json_request_file, id):
		entity_url = entity_url.replace("_env_", config.env[self.__env__])
		entity_url = entity_url.replace("_id_", id)

		requests.packages.urllib3.disable_warnings()	# si verify=False
		
		try:
			entity = open(entity_json_request_file)
			response = requests.post(entity_url.replace("_id_", id), verify=False)#certifi.where())
			entity.close()	
		except FileNotFoundError:
			raise RuntimeError(f"Archivo {entity_json_request_file} inválido o no existe")

		return response
