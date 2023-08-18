from sys import path
from sys import argv

from api import api

path.append('./paquete')
path.append('prestamo')



def main():

    if len(argv) != 3:
        print("Faltan argumentos para correr el programa\nUso: python3 main.py <tipo solicitud> <ambiente>")
        return
    
    app = api.API(argv[1], argv[2])
    app.alta()

main()
    
