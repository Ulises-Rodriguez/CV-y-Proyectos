//selecciono los elemntos dentro para crear publicaciones:
//parte q selecciona los datos
const allContainer = document.getElementById("all-container");
const publicationContainer = document.getElementById("publication-container");
let nombreCrear = document.getElementById("text-name");
let edadCrear = document.getElementById("text-age");
let estadoCivilCrear = document.getElementById("text-civil-status");
let comidaFavoritaCrear = document.getElementById("text-food");
let comentarioCrear = document.getElementById("text-comment");
//parte q selecciona los botones
const botonCrear = document.getElementById("botonCrear");
const botonBorrar = document.getElementById("botonBorrar");

//esta parte seria la q se encargaria de tomar los datos de la parte de crear datos o publicaciones
const crearPublicacion = ()=>{
    //creo q tengo q ser mas especifico con el fetch para inddicarle q solo tome los datos q estan dentro del div de crear publicacion (investigar)
    const peticion = fetch("http://localhost/proyectos/fetch/fetch.html",{
        method : "POST",
        body : JSON.stringify({
            "nombre" : nombreCrear.value,
            "edad" : edadCrear.value,
            "estado civil" : estadoCivilCrear.value,
            "comida favorita" : comidaFavoritaCrear.value,
            "comentario" : comentarioCrear.value
        }),
        headers : {"Content-type":"application/json"}
    });

    //igual falta ver como hacer para q los datos tomados se escriban solos en el archivo info.txt (capaz para esto hay q usar node.js o algo por el estilo investigar esto mas tarde)
    peticion
        .then(res=>res.json())
        .then(res=>console.log(res))
        .catch(rej=>console.log("lo siento ha ocurrido un error"));
};



//añado los eventos a los botones de crear publicacion 
botonCrear.addEventListener("click",()=>{
    crearPublicacion();
});

botonBorrar.addEventListener("click",()=>{
    nombreCrear.value = "";
    edadCrear.value = "";
    estadoCivilCrear.value = ""; 
    comidaFavoritaCrear.value = "";
    comentarioCrear.value = "";
});

//esta parte es la encargada de crear y cargar las publicaciones almacenadas en el info.txt
const crearElementos = (nombre,edad,ec,cf,comentario)=>{
    //info de la publicacion
    let divPublicacion = document.createElement("div");
    let divUserContainer = document.createElement("div");
    let divUser = document.createElement("div");
    let divTextContainer = document.createElement("div");
    let divText = document.createElement("div");    
    
    //input y boton para hacer comentarios
    //esto tiene el mismo problema q lo de crearPublicacion, falta ver como hacer para q el comentario se escriba en el info.txt
    let divCommnetPublicationContainer = document.createElement("div");
    let inputTextPublication = document.createElement("input");
    let buttonTextPublication = document.createElement("button");

    //agrego calses a los elementos
    divPublicacion.classList.add("publication");
    divUserContainer.classList.add("user-container");
    divUser.classList.add("user");
    divTextContainer.classList.add("text-container");
    divText.classList.add("text");

    divCommnetPublicationContainer.classList.add("commnet-publication-container");
    inputTextPublication.classList.add("text-publication");
    buttonTextPublication.classList.add("text-publication-button");

    //agrego el type y placeholder al input y button
    inputTextPublication.type = "text";
    buttonTextPublication.type = "submit";

    //agrego los valores o el contenido q va a tener cada uno
    divUser.textContent = `nombre: ${nombre}`;
    divText.innerHTML = `edad: ${edad}<br>
                         estado civil: ${ec}<br>
                         comida favorita: ${cf}<br>
                         comentario: ${comentario}`;

    inputTextPublication.placeholder = "Escriba aqui su comentario";
    buttonTextPublication.textContent = "Comentar";

    //agrego los hijos a los padres (buscar una forma mejor de comentar esto xq suena muy raro XD)

    publicationContainer.appendChild(divPublicacion);
    divPublicacion.appendChild(divUserContainer);
    divUserContainer.appendChild(divUser);

    divPublicacion.appendChild(divTextContainer);
    divTextContainer.appendChild(divText);

    divPublicacion.appendChild(divCommnetPublicationContainer);
    divCommnetPublicationContainer.appendChild(inputTextPublication);
    divCommnetPublicationContainer.appendChild(buttonTextPublication);

    return divPublicacion;
};

//practica con intersection observer (esto para q cargue las publicaciones de forma automatica a medida q se vaya haciendo scrool hacia abajo)
const callbackPublis = entries=>{
    const entry = entries[0];

    //lo q dice esta parte es q si se est viendo el primer bloque (q como es un array el primero es el 0) entonces q se llama a la funcion "cargarPublicaciones" y q esta cargue 3 publicaciones de "info.txt"
    if (entry.isIntersecting) {
        console.log(entry.isIntersecting);
        cargarPublicaciones(3);
    }
}

const observar = new IntersectionObserver(callbackPublis);

//esta parte es la encargada de hacer q se carguen las publicaciones almacenadas en info.txt
let contador = 0;

const cargarPublicaciones = async (num)=>{

    const peticionPublicaciones = await fetch("info.txt");
    const arrayContent = await peticionPublicaciones.json();
    const array = arrayContent.content;
    const documentFragment = document.createDocumentFragment();
    console.log(array);

    for (let i = 0; i < num; i++) {
        if (array[contador] != undefined) {
            const nuevaPublicacion = crearElementos(array[contador].nombre,array[contador].edad,array[contador].estadoCivil,array[contador].comidaFavorita,array[contador].comentario);
            documentFragment.appendChild(nuevaPublicacion);
            contador++;

            if (i == num-1) {
                observar.observe(nuevaPublicacion);
            }
        }
        else{
            const noMasPublis = document.createElement("b");

            noMasPublis.textContent = "No hay mas publicaciones";
            noMasPublis.classList.add("no-more");
            allContainer.appendChild(noMasPublis);
            break
        }
    }
    publicationContainer.appendChild(documentFragment);
};

cargarPublicaciones(3);