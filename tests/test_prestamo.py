import pytest
import prestamo
import sys
sys.path.insert(1, '/..')
from config import *
sys.path.append('/../prestamo')
import prestamo


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
	solicitud_response = prestamo.post("Solicitud", URL_SOLICITUD, '../solicitud04.json', "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])
	prestamo_response = prestamo.post("Prestamo", URL_PRESTAMO, '../prestamo.json', id_solicitud)

	assert prestamo_response.status_code == 200


def test_prestamo_86_post_success():
	solicitud_response = prestamo.post("Solicitud", URL_SOLICITUD, '../solicitud86.json', "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])
	prestamo_response = prestamo.post("Prestamo", URL_PRESTAMO, '../prestamo.json', id_solicitud)

	assert prestamo_response.status_code == 200


def test_prestamo_04_file_not_found_exception():
	solicitud_response = prestamo.post("Solicitud", URL_SOLICITUD, '../solicitud04.json', "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])

	with pytest.raises(RuntimeError):
		prestamo.post("Prestamo", URL_PRESTAMO, 'prestamo04.json', id_solicitud)


def test_prestamo_invalid_request_body_exception():
	'''Espera a que se levante un ValueError tras enviar como requerimiento un prestamo inválido (tipoPrestamo = null).'''
	solicitud_response = prestamo.post("Solicitud", URL_SOLICITUD, '../solicitud86.json', "")
	id_solicitud = str(solicitud_response.json()['idSolicitud'])

	with pytest.raises(ValueError):
		prestamo.post("Prestamo", URL_PRESTAMO, 'prestam0.json', id_solicitud)