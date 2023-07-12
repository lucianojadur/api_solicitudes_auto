from escape_codes import *

env = {
	"local": "localhost:28007",
	"inte": "10.164.20.232",
	"homo": "solicitudes.sis.ad.bia.itau"
}

id_solicitud = ""
URL_SOLICITUD       = "http://_env_/apiSolicitudes/solicitud/"
URL_CLIENTE         = "http://_env_/apiSolicitudes/solicitud/_id_/cliente/"
URL_AUMENTO_LINEA   = "http://_env_/apiSolicitudes/solicitud/_id_/aumentoLinea/"
URL_PAQUETE         = "http://_env_/apiSolicitudes/solicitud/_id_/paquete/"
URL_PRESTAMO        = "http://_env_/apiSolicitudes/solicitud/_id_/prestamo/"
URL_CCOMITENTE      = "http://_env_/apiSolicitudes/solicitud/_id_/cuentaComitente/"

URL_ENVIAR			= "http://_env_/apiSolicitudes/solicitud/_id_/enviar/"



CLIENTE_PATH = 'cliente/cliente.json'
PRESTAMO_PATH = 'prestamo/prestamo.json'
PAQUETE_PATH = 'paquete/paquete.json'

entity = {
	"02": ("Paquete", URL_PAQUETE, PAQUETE_PATH),
	"03": ("Cuenta comitente", URL_CCOMITENTE, ".."),
	"04": ("Prestamo", URL_PRESTAMO, PRESTAMO_PATH),
	"86": ("Prestamo", URL_PRESTAMO, PRESTAMO_PATH)
}




def error_connection_msg():
	print(CODE[5] + "Error de conexión con la API. Chequear que esté activa." + CODE[0])
