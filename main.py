from sys import path
from sys import argv

path.append('./paquete')
path.append('prestamo')

import paquete.paquete as Paquete
import prestamo.prestamo as Prestamo

alta = {
    "02": Paquete,
    "04": Prestamo,
    "86": Prestamo,
}


def main():

    if len(argv) < 2:
        print("Faltan argumentos para correr el programa")
        return
    alta[argv[1]].alta(argv[1])


main()
    
