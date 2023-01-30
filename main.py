from sys import path
from sys import argv

path.append('./paquete')
path.append('prestamo')

import producto.producto as producto



def main():

    if len(argv) < 2:
        print("Faltan argumentos para correr el programa")
        return
    producto.alta(argv[1])


main()
    
