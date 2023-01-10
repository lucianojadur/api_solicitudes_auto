import escape_codes

id_solicitud = ""
URL_SOLICITUD       = "http://localhost:28007/apiSolicitudes/solicitud/"
URL_CLIENTE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cliente/"
URL_AUMENTO_LINEA   = "http://localhost:28007/apiSolicitudes/solicitud/_id_/aumentoLinea/"
URL_PAQUETE         = "http://localhost:28007/apiSolicitudes/solicitud/_id_/paquete/"
URL_PRESTAMO        = "http://localhost:28007/apiSolicitudes/solicitud/_id_/prestamo/"
URL_CCOMITENTE      = "http://localhost:28007/apiSolicitudes/solicitud/_id_/cuentaComitente/"

URL_ENVIAR			= "http://localhost:28007/apiSolicitudes/solicitud/_id_/enviar/"



def error_connection_msg():
	print(CODE[5] + "Error de conexión con la API. Chequear que esté activa." + CODE[0])
