import requests


URL_SOLICITUD       = "http://localhost:28007/apiSolicitudes/solicitud/915"
URL_CLIENTE         = "http://localhost:28007/apiSolicitudes/cliente/"
URL_AUMENTO_LINEA   = "http://localhost:28007/apiSolicitudes/aumentoLinea/"
URL_PAQUETE         = "http://localhost:28007/apiSolicitudes/paquete/"
URL_PRESTAMO        = "http://localhost:28007/apiSolicitudes/prestamo/"
URL_CCOMITENTE      =  "http://localhost:28007/apiSolicitudes/cuentaComitente/"

SOLICITUD_BODY = {
  "tipoSolicitud": "86",
  "codigoCanal": "O",
  "codigoOficial": "BR4R",
  "codigoSucursal": "04",
  "codigoGestionDocumental": "CRM421905719125653",
  "monto": "100009.99",
  "origen": "6546",
  "motivoRecepcion": "PLD",
  "estado": "02",
  "excepcion": "false"
}

req = requests.get("http://localhost:28007/apiSolicitudes/solicitud/915")

print(req.json) 

def test_post_solicitud_success():
    resp = requests.post(URL_SOLICITUD, json=SOLICITUD_BODY)
    assert req.status_code == 200