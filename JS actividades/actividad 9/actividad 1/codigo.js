const inputNombre = document.querySelector(".nombre");
const btnAñadir = document.querySelector(".btn-añadir");
const nombresContainer = document.querySelector(".nombres-container");

let nombreFormateado = "";
const arrayDeNombres = [];

const convertirNombre = () => {
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

const añadirNombreArray = (nombre, array) => {

    if (comprobarNombre(nombreFormateado, array)) {
        array.push(nombreFormateado);
        console.log(array);

        const divNombre = document.createElement("div");
        divNombre.classList.add("array-nombre");
        divNombre.textContent = array[array.length - 1];

        nombresContainer.appendChild(divNombre);
        nombresContainer.style.visibility = "visible";

    } else {
        alert("El nombre que se intenta añadir ya esta en la lista");
    }

}

const vaciar = () => {
    inputNombre.value = "";
    inputNombre.focus();
}

inputNombre.addEventListener("keydown", (e) => {
    if (e.key == "Enter") {
        convertirNombre();
        añadirNombreArray(nombreFormateado, arrayDeNombres);
        vaciar();
    }
});

btnAñadir.addEventListener("click", () => {
    convertirNombre();
    añadirNombreArray(nombreFormateado, arrayDeNombres);
    vaciar();
});