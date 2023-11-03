# ahora q es un paquete --> una carpeta con muchos modulos python
# para q python se de cuenta q es un paquete dentro de la carpeta con muchos modulos creas un archivo __init__.py
import paquete.suma
import paquete.resta

print(paquete.suma.suma(2, 2))
print(paquete.resta.resta(2, 2))

# si tenes una carpeta dentro de otra
# import paquete.subcarpta.archivo y no te olvides de crearle su __init__.py
