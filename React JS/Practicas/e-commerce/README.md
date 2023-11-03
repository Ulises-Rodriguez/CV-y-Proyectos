# Proyecto Final React JS (e-commerce)

## Nombre de la pagina: *La Friki Cueva*

### Dependencia extras por npm:
1. Bootstrap 
    >La use debido a q facilitaba la creacion de navbar y me ahorraba tiempo en el css
2. Firebase
    >EN un principio tenia todos mis productos en el .json y los trai con useFetch (mi hook perzonalizado) pero luego tuvimos q cambiar a firebase
3. React Router DOM
    >Para poder hacer el ruteo de la app
4. Sweetalert2
    >Para mostrar unos alerts mas agredables a la vista

### Video de como usar la pagina:
    >Youtube : https://youtu.be/gT5LTm-6rBg

### Ideas/Enfoques:
1. En App.jsx se ecnuentra el wrapper del contexto para que todos los componentes hijos puedan acceder a las vairiables como "cliente" o "cart", el Layout (encargado de mostrar el navbar y footer en todas las pages) y el ruteo de las diferentes pages

2. Dentro del contexto esta la informacion del cliente (que se modifica al completar el formulario de compra) y el cart (que es donde se van guardando los productos y el precio total)

3. Las funciones usadas dentro de los componentes Home, Figura, ConsolaDettale, JuegosDetalle:
    
    1. cargar es una funcion para mostrar el mensaje de cargando los productos y el spinner (componente Loading), luego de pasar el tiempo se muestran toda la lista de productos

    2. useGetFSC es un hook perzonalizado que se encarga se encarga de obtener los productos cargados en firestore (dependiendo cual sea el el string que se le pase como argumento). La idea de crear un hook personalizado fue debido a que el codigo dentro del hook se repetia en muchos componentes y de esta manera el codigo dentro de cada componente quedaba mas limpio y no era necesario escribir el mismo codigo varias veces

    3. se usa el metodo map() para generar todos los Items de manera dinamica y no tener que estar repitiendo el mismo componente una y otra ves

4. El componente Item es el encargado de tomar los datos y crear las tarjetas de presentacion de los productos, debido a que algunas descripciones de los productos eran mas largas que otras Item recive como prop estilos para que de esta manera no todo el contenido de los productos quede dentro de las tarjetas.
    
    1. A su ves dentro del componente Item se llaman a otros 3 componentes : Counter, BtnDetalle, BtnAñadir

        1. Counter: es un componente que se encarga de los btn para indicar cuanto de un mismo producto queremos añadir (no permitiendo que se agreguen numero negativos y que no se pase del stock disponible), tambien modificando la variable cantidad que se utiliza como condicion en BtnAñadir

        2. BtnDetalle: es un componente que junto con DetalleProducto permiten ver los productos de forma individual

        3. BtnAñadir: como su nombre indica es el componente que se encarga de añadir los productos al carrito, modificando a su ves el contenido de la variable cart (que se encuentra en el contexto)
            
            1. La funcion añadir del evento click del btn primero se encarga de ver si la cantidad es mayor a 0 para no permitir añadir 0 de un producto, luego comprobar si el producto ya esta añadido al carrito en caso de estarlo modifica la cantidad de ese producto y en caso de que no este lo añade al carrito

5. DetalleProducto: es el componente en cargado que muestra el detalle de cada producto de forma individual

    1. Dentro tiene una funcion obtenerProducto que como su nombre indica obtiene la info del producto individual

    2. ComprobarCategoria: su valor retornado varia dependiendo el apartado de la pagina que queremos entrar (en caso de por ejem ser consolas necesita hacer una segunda busqueda de producto) 

6. El componente NotFound es el que se usa para en caso de que no se encuentre la ruta elegida, tuve que crear este componente debido a como trabaja el componente DetalleProducto con useParams con el id.

    ejem: si intentba ingresar a "/asd" no ha ningun producto que coincida con ese id pero la ruta para el detalle de los productos de home (para este ejem) toma como id=asd, intenta buscar el producto (retorna undefined ya que no lo encuentra) y cargaba el Layout y el resto de la pagina en blanco.

    Debido a DetalleProducto la ruta "<Route path='*' element={<NotFound/>} />" (que se encarga de capturar todas las rutas que no esten creadas y mostrar un msg de "ruta no encontrada") nunca se ejecutaba ya que si bien "/asd" no hay producto con ese id DetalleProducto lo capturaba igual

7. CardWidget: es el componente del carrito de compras dentro de el estan los componentes:

    1. CantidadProductos: que es el numerito que indica la cantidad de productos añadidos

    2. CartImg: la imagen del carrito

    3. CarritoLi: que son los productos con su nombre y cantidad de estos que se añadieron (estos se generan de manera automatica con un map en el array de cart["productos"])

    4. Precio: que se encarga de mostrar el precio total de todos los productos sumados (se usa el meotod Math para redondear el valor)

    5. BtnOpcion: es el componente que da funcionalidad a los btns del carrito que dependiendo del la prop que se le pase resetea el carrito y cliente o te redirije al resumen de compra y formulario para ingresar los datos para realizar la compra (y que esta se añada a firestore) 

8. Checkout: es el componente donde se encuentra el resumen de compra, formulario y btns para realizar la compra o resetear el carrito

    1. ResumenCompra: muestra el resumen de compra con los productos, su cantidad, precio total, unitario y el precio total de la suma de todos los productos.
    Con map se genera la lista con la info de los productos dentro de cart

    2. Formulario: es el componente encargado de modificar los valores de la varibale "cliente" que luego son usados para cargar la infor del comprador en firestore

    3. BtnRealizarCompra: se encarga de agregar el docuento a la coleccion ordenes a firestore. Tambien se encarga de mostrar el ID de compra en un sweetalert (en caso de que alguno de los campos falte o los emails no coincidan se lanza un sweetalert con un mensaje indicando el error y no permitiendo que se guarde la info de la orden en firestore)

        1. Para realizar la compra lo trabaje con async y await debido a que al JS trabaja de forma asincrona en lo que terminaba de hacer la peticion para guardar la info de la orden seguia ejecutando otras lineas de codigo (la del sweetaler con el mensaje de compra realizada y mostrar ID) por lo cual el ID de la orden de compra se obtenia luego de que se ejecutara este sweetalert y nunca llegaba a mostrar el ID de la orden de compra. Por lo cual fue necesario volver la esta parte sincrona para evitar la ejecucion del sweetalert hasta que no terminara la peticion para guardar la orden y obtener le ID

9. Use bastante el uso del spread operator para no tener que copiar a mano todos los elementos de los objetos o array 