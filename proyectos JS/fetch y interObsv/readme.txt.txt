Hola para poder hacer cambios hace falta tener un servidor en mi caso use XAMPP

En este proyecto la idea fue hacer como una especie de red social o algo por el estilo (todavia no esta terminada debido
a q me falta aprender hacer la parte q permite crear nuevas publicaciones y q se agreguen por si solas al archivo llamado
"info.txt"), en este use la API Fetch y IntersectionObserver

En la pagina se van a encontrar con el primer bloque rojo q seria la encargada de crear nuevas publicaciones

Luego las cajas de color azul es donde se carga o pone la informacion almacenada en el archivo "info.txt" q harian como
si fueran publicaciones de personas (tambien falta la parte en la q permite hacer comentarios sobre las publicaciones
q se van cargando 

Las publicaciones se van cargando de forma automatica (de 3 en 3) hasta q ya no alla mas contenido q cargar del archivo
"info.txt" una vez esto pasa aparece un mensaje q inica q ya no hay mas publicaciones

Aclariacion: puede pasar q si la pantalla de donde estas mirando esto es muy grande entonces no se te carguen el resto de 
las publicaciones, en caso de tener este problema entrar al archivo llamado "codigo.js" ir hasta la ultima linea (en mi
caso la 153) y cambiar el numero 3 de la funcion llamada "cargarPublicaciones(3);" por uno mayor (creo q 5 deberia
andar bien)

Aclaracion2: en el archivo "info.txt" hay un total de 16 elemenetos, si se quiere ver un efecto de cargar mas largo 
modificar este archivo agregando mas elementos     

Aclaracion3: en el archivo "codigo.js" pienso ir poniendo comentarios en los cuales voy a ir explicando que hace cada parte
del codigo (voy a tratar de explicarlo de tal manera q alguien q tenga pocos conocimientos de programacion en general pueda
darse una idea de como funciona, por lo cual la explicacion va a estar hecha en su mayor parte usnado mis palabras y no 
tanto un habla tecnica)

Aclaracion4: en el archivo "coigo.js" hay partes q se pueden optimizar o q sobran o hay q modificar(ejem: los console.log)
asi q pienso ir depurando el codigo para q quede mejor y mas facil e leer

Un saludo y cualquir comentario o mejora q crean q se le puede hacer es bienvenida