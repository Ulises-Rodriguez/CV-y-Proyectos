const inputNombre = document.querySelector(".nombre");
const btnAñadir = document.querySelector(".btn-añadir");
const nombresContainer = document.querySelector(".nombres-img-container");

let nombreFormateado = "";
const arrayDeNombres = [];

const arrayImg = [
    {
        name: "Atanagildo",
        img: "https://www.html6.es/img/rey_atanagildo.png",
    }, {
        name: "Ataulfo",
        img: "https://www.html6.es/img/rey_ataulfo.png",
    }, {
        name: "Ervigio",
        img: "https://www.html6.es/img/rey_ervigio.png",
    }, {
        name: "Leogivildo",
        img: "https://www.html6.es/img/rey_leogivildo.png",
    }, {
        name: "Leogivildo",
        img: "https://www.html6.es/img/rey_leogivildo.png",
    }, {
        name: "Recesvinto",
        img: "https://www.html6.es/img/rey_recevinto.png",
    }, {
        name: "Sisebuto",
        img: "https://www.html6.es/img/rey_sisebuto.png",
    }, {
        name: "Teodorico",
        img: "https://www.html6.es/img/rey_teodorico.png",
    }]
    const convertirNombre = () => {
        debugger
        const nombre = inputNombre.value.trim();
    nombreFormateado = nombre.substring(0, 1).toUpperCase() + nombre.substring(1).toLowerCase();
}

const comprobarNombre = (nombre, array) => {

    let res = true;

    if (array.length != 0) {
        if (array.some(element => element == nombre)) {
            res = false;
        }
    }

    return res;
}

const añadirImg = (nombre, array) => {
    const defaultImg = "https://www.html6.es/img/rey_incognito.png";

    for (let i = 0; i < array.length; i++) {
        if (nombre == array[i].name) {
            return array[i].img;
        }
    }

    return defaultImg

}

const añadirNombre = (nombre, array) => {

    debugger
    if (comprobarNombre(nombre, array)) {
        array.push(nombre);

        const imgRey = añadirImg(nombre, arrayImg);

        const pNombre = array[array.length - 1];

        nombresContainer.insertAdjacentHTML("beforeend", `<div class="div-contenedor">
        <img src=${imgRey}>
        <b class="nombre-rey">${pNombre}</b>
        </div>`);

        let ultimo = document.querySelectorAll(".div-contenedor").length-1;

        document.querySelectorAll(".div-contenedor")[ultimo].onclick=eliminar;

        nombresContainer.style.visibility = "visible";

    } else {
        alert("El nombre que se intenta añadir ya esta en la lista");
    }

}

const eliminar = ()=>{
    
    const texto = this.querySelector(".nombre-rey");
    const buscar = arrayDeNombres.indexOf(texto);

    arrayDeNombres.splice(buscar,1);

    this.remove();
}

const vaciar = () => {
    inputNombre.value = "";
    inputNombre.focus();
}

inputNombre.addEventListener("keydown", (e) => {
    if (e.key == "Enter") {
        convertirNombre();
        añadirNombre(nombreFormateado, arrayDeNombres);

        vaciar();
    }
});

btnAñadir.addEventListener("click", () => {
    convertirNombre();
    añadirNombre(nombreFormateado, arrayDeNombres);

    vaciar();
});
