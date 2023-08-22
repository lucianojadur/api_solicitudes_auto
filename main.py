from sys import path
from sys import argv

from api import api
from escape_codes import *

path.append('./paquete')
path.append('prestamo')



def main():

    if len(argv) != 3:
        if len(argv) == 2 and argv[1].isdigit():
            argv.append("inte")
        else: 
            print(f"{COLOR[4]}Faltan argumentos para correr el programa\nUso:~$ python3 main.py <tipo solicitud> <ambiente>{COLOR[0]}")
            return
    print(f"Ejecución en {COLOR[6] + argv[2].upper() + COLOR[0]}\n")
    app = api.API(argv[1], argv[2])
    app.alta()

main()
    
