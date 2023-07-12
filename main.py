from sys import path
from sys import argv

path.append('./paquete')
path.append('prestamo')

import producto.producto as producto



def main():

    if len(argv) != 3:
        print("Faltan argumentos para correr el programa\nUso: python3 main.py <tipo solicitud> <ambiente>")
        return
    
    producto.alta(argv[1], argv[2])


main()
    
