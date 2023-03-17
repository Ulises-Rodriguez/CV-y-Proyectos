const imgRojo = "https://www.html6.es/img/rojo.png";
const imgAzul = "https://www.html6.es/img/azul.png";


const btnAñadirRojo = document.querySelector(".añadirRojo");
const btnAñadir4Azules = document.querySelector(".añadir4Azules");
const btnModificarAzules = document.querySelector(".modificarAzules");
const btnEliminarRojos = document.querySelector(".eliminarRojos");
const btnVaciar = document.querySelector(".vaciar");

const imgContainer = document.getElementById("img-container");
imgContainer.style.border = "none";

btnAñadirRojo.addEventListener("click", () => {
    //creo la imagen a agregar
    const imgChoeteRojo = document.createElement("img");
    //le doy atributos
    imgChoeteRojo.setAttribute("src", imgRojo);
    imgChoeteRojo.classList.add("choete-rojo");

    //cambio estilos del container de las imagenes
    if (imgContainer.style.border === "none") {
        imgContainer.style.border = "solid #000 2px";
    }
    //agrego el elemento hijo al contenedro padre
    imgContainer.appendChild(imgChoeteRojo);
});

btnAñadir4Azules.addEventListener("click", () => {
    for (let i = 0; i < 4; i++) {
        //creo la imagen a agregar
        const imgHtml6Azul = document.createElement("img");
        //le doy atributos
        imgHtml6Azul.setAttribute("src", imgAzul);
        imgHtml6Azul.classList.add("html6-Azul");

        //cambio estilos del container de las imagenes
        if (imgContainer.style.border === "none") {
            imgContainer.style.border = "solid #000 2px";
        }
        //agrego el elemento hijo al contenedro padre
        imgContainer.appendChild(imgHtml6Azul);
    }
});

btnModificarAzules.addEventListener("click", () => {
    for (let i = 0; i < imgContainer.childNodes.length; i++) {
        if (imgContainer.children[i].className === "html6-Azul") {
            imgContainer.children[i].src = imgRojo;
            imgContainer.children[i].className = "choete-rojo";
        }
    }
});

btnEliminarRojos.addEventListener("click", () => {

    //recorremos desde el final hasta el pricncipio xq en el caso de recorrer del primero al ultimo cuando i=0 eliiminamos el primer elemento el segundo elemento pasa a ser el primero (osea q si su posicion era 1 ahora es 0) por lo cual cuando i=1 no hay nada en la posicion 1

    const contador = document.querySelectorAll(".choete-rojo").length;
    for (let i = contador - 1; i >= 0; i--) {
        document.querySelectorAll(".choete-rojo")[i].remove();
    }
    if (!imgContainer.children) {
        imgContainer.style.border = "none";
    }
});

btnVaciar.addEventListener("click", () => {
    //cambio el estilo de container de las imganes
    if (imgContainer.style.border !== "none") {
        imgContainer.style.border = "none";
    }

    //uso un bucle while para q mientras tenga elementos el container imagenes se va a ejecutar y por cada vuelta elimina un elemento hijo
    while (imgContainer.lastChild) {
        imgContainer.removeChild(imgContainer.lastChild);
    }
});