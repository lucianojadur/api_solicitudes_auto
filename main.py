import requests


req = requests.get("http://localhost:28007/apiSolicitudes/solicitud/915")

print(req.json) 

