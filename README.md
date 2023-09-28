# API Solicitudes auto ![](https://img.shields.io/github/v/release/lucianojadur/api_solicitudes_auto?color=brightgreen&style=plastic)


Esto es básicamente un script para automatizar el flujo de request enviados a **API_SOLICITUDES** del banco ITAU AR para los principales productos a solicitar.



Ejecución:

0. (en caso de estar parado fuera del directorio del proyecto):
```bash
    cd mi/directorio/padre/de/api_solicitudes_auto
```
1. (desde el directorio raíz del proyecto):
```bash

    python app.py [xx] [env]
```

donde  
    - ```xx``` es un número entero de 2 dígitos que indica el tipo de solicitud/producto a generar.  
    - ```env``` es una palabra que indica el ambiente de prueba. Sus posibles valores son:  
    &emsp;&emsp; ```local```: la aplicación corriendo en un puerto local  
    &emsp;&emsp; ```inte```: integración  
    &emsp;&emsp; ```homo```: homologación

