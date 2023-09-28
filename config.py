from escape_codes import *

env = {
	"local": "localhost:28007",
	"inte": "solicitudesinte.sis.ad.bia.itau",
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
	"30": ("Seguro Compra Protegida", URL_SEGURO, SEGURO_JSON_PATH),
	"31": ("Seguro Protección Móvil", URL_SEGURO, SEGURO_JSON_PATH),
	"32": ("Seguro Accidentes Personales", URL_SEGURO, SEGURO_JSON_PATH),
	"33": ("Seguro Hogar", URL_SEGURO, SEGURO_JSON_PATH),
	"34": ("Seguro Bolso Protegido", URL_SEGURO, SEGURO_JSON_PATH),
	"35": ("Seguro Vida CGA", URL_SEGURO, SEGURO_JSON_PATH),
	"36": ("Seguro Movilidad Sura", URL_SEGURO, SEGURO_JSON_PATH),
	"37": ("Seguro Personal Bank", URL_SEGURO, SEGURO_JSON_PATH),
	"38": ("Seguro Integral de Negocios (PF)", URL_SEGURO, SEGURO_JSON_PATH),
	"39": ("Seguro Integral de Consorcios (PF)", URL_SEGURO, SEGURO_JSON_PATH),
	"40": ("Seguro PUA", URL_SEGURO, SEGURO_JSON_PATH),
	"41": ("Seguro Auto", URL_SEGURO, SEGURO_JSON_PATH),
	"86": ("Prestamo", URL_PRESTAMO, PRESTAMO_JSON_PATH)
}


def error_connection_msg():
	print(COLOR[5] + "Error de conexión con la API. Chequear que esté activa." + COLOR[0])
