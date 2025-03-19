import pytest

import sys
sys.path.append('../')
from config import *
sys.path.append('../api')
from api import API


SOLICITUD_04_PATH = '../solicitudes/solicitud04.json'
SOLICITUD_86_PATH = '../solicitudes/solicitud86.json'
PRESTAMO_PATH = '../prestamo/prestamo.json'



PRESTAMO_BODY = {
	"tipoPrestamo": "APERS",
	"cuenta": "10014773014",
	"producto": "1110907",
	"moneda": "ARP",
	"importe": 1000000,
	"cantidadCuotas": 24,
	"vencimiento": "04",
	"cuentaDebito": "10014773014",
	"cuentaCredito": "10014773014",
	"codigoSeguroVida": "99",
	"codigoDestinoFondos": "0009",
	"montoMaximoDispCliente": 3000000,
	"montoMaximoCuotaCliente": 204568
}


def test_prestamo_04_post_success():
	solicitud_response = API.post("Solicitud", URL_SOLICITUD, SOLICITUD_04_PATH, "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])
	prestamo_response = API.post("Prestamo", URL_PRESTAMO, PRESTAMO_PATH, id_solicitud)

	assert prestamo_response.status_code == 200


def test_prestamo_86_post_success():
	solicitud_response = API.post("Solicitud", URL_SOLICITUD, SOLICITUD_86_PATH, "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])
	prestamo_response = API.post("Prestamo", URL_PRESTAMO, PRESTAMO_PATH, id_solicitud)

	assert prestamo_response.status_code == 200


def test_prestamo_04_file_not_found_exception():
	solicitud_response = API.post("Solicitud", URL_SOLICITUD, SOLICITUD_04_PATH, "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])

	with pytest.raises(RuntimeError):
		API.post("Prestamo", URL_PRESTAMO, 'prestamo04.json', id_solicitud)


def test_prestamo_invalid_request_body_exception():
	'''Espera a que se levante un ValueError tras enviar como requerimiento un prestamo inválido (tipoPrestamo = null).'''
	solicitud_response = API.post("Solicitud", URL_SOLICITUD, SOLICITUD_86_PATH, "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])

	with pytest.raises(ValueError):
		API.post("Prestamo", URL_PRESTAMO, 'prestam0.json', id_solicitud)
