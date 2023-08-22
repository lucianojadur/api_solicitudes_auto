from escape_codes import *

env = {
	"local": "localhost:28007",
	"inte": "10.164.20.232",
	"homo": "solicitudeshomo.sis.ad.bia.itau"
}

id_solicitud = ""
URL_SOLICITUD       = "https://_env_/apiSolicitudes/solicitud/"
URL_CLIENTE         = "https://_env_/apiSolicitudes/solicitud/_id_/cliente/"
URL_AUMENTO_LINEA   = "https://_env_/apiSolicitudes/solicitud/_id_/aumentoLinea/"
URL_PAQUETE         = "https://_env_/apiSolicitudes/solicitud/_id_/paquete/"
URL_PRESTAMO        = "https://_env_/apiSolicitudes/solicitud/_id_/prestamo/"
URL_CCOMITENTE      = "https://_env_/apiSolicitudes/solicitud/_id_/cuentaComitente/"
URL_SEGURO			= ""

URL_ENVIAR			= "https://_env_/apiSolicitudes/solicitud/_id_/enviar/"

import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
CERT = dir_path + '/sis-ad-bia-itau.pem'


CLIENTE_JSON_PATH = 'cliente/cliente.json'
PRESTAMO_JSON_PATH = 'prestamo/prestamo.json'
PAQUETE_JSON_PATH = 'paquete/paquete.json'
AUMENTO_JSON_PATH = 'aumento_linea/aumento_linea.json'
SEGURO_JSON_PATH = ''

NAME = 0
URL = 1
JSON_PATH = 2

entity = {
	"01": ("Aumento de Línea", URL_AUMENTO_LINEA, AUMENTO_JSON_PATH),
	"02": ("Paquete", URL_PAQUETE, PAQUETE_JSON_PATH),
	"03": ("Cuenta comitente", URL_CCOMITENTE, ".."),
	"04": ("Prestamo", URL_PRESTAMO, PRESTAMO_JSON_PATH),
	"29": ("Seguro ATM", URL_SEGURO, SEGURO_JSON_PATH),
	"86": ("Prestamo", URL_PRESTAMO, PRESTAMO_JSON_PATH)
}


def error_connection_msg():
	print(COLOR[5] + "Error de conexión con la API. Chequear que esté activa." + COLOR[0])
