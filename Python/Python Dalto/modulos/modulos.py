# todo los archivos q terminan en .py son modulos
# les decimos modulos xq desde un modulo podemos llamar a otro o crear otro, cambiar las rutas, formar paquetes de modulos
# ejem: si tengo un modulo con muchas funciones para no tener q crearlas denuevo llama al modulo 1 dentro de modulo 2 y podes usar las funciones q estan dentro del modulo 1
# modular es basicamente separar el codigo en partes (como los componentes en react) q cada modulo se haga cargo de una parte del codigo en general

# tenemos 3 modulos, los modulos de python q ya vienen incorporados de por si (estan escritos en C) y despues tenemos los third parties modulos q serian los modulos creados por terceros (modulos q crea la gente y vos descargas y usas) y por ultimo estan los own modulos q son los modulos q creas vos

# 1) para poder usar las funciones dentro de otros modulos tenes q importarlos
# import saludar as modulo_saludo
import modulo_saludar as ms

# 2) ahora imagina q tenes un modulo con mucho contenido pero solo necesitas una funcion en particular de ese modulo, entonces para no importar todo el modulo y hacer q el programa se vuelva mas pesado podes llamar solo a la funcion con from
from modulo_importar_una_funcion import suma, resta
# tambien podes renombrarlas con as --> suma as s, resta as r

# 3) para movernos entre carpetas lo hacemos con el .
from modulo_dentro_carpeta.modulo1 import saludo_modulo_1

# 4) ahora q pasa si el modulo al q queremos acceder esta dentro de una carpeta q esta al mismo nivel q la carpeta q contiene al modulo q llama al otro
# para esto usamos sys
import sys
import saludar


# 1)
# como veras al importarlo la funcion saludo ahora es un metodo y se lo llama como tal
# para ahorrarte el laburo de tenes q llamas modulo_saludar podes usar el as para cambiarla el nombre, esto tambien es util por si tenes q crear una variable con el mismo nombre
# saludo = modulo_saludar.saludo("Juan")
saludo = ms.saludo("Juan")
print(saludo)

# 2)
# si te fijas se te creo una carpeta llamada __pycache__ es para q ande mas rapido
res = suma(2, 3)
print(res)

res = resta(2, 3)
print(res)

# 3)
saludo_modulo_1("Hola todo bien?")

# 4)
# con esto obtenes la ruta de donde esta este modulo
# print(sys.path)
# ahora copia el primer elemento del array y cambiale el nombre de lo q viene despues de las \\
# esta es la ruta donde se aloja el modulo2 dentro de modulo_mismo_nivel
sys.path.append('c:\\Users\\Uli\\Desktop\\Python Dalto\\funciones_buenas')
# print(modulo_saludo.saludar("Hola"))
print(sys.path)

saludar.saludar("jhsdfjksdhghgjk")
