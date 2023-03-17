const magdalena = document.createElement("img");
magdalena.src = "https://www.html6.es/img/pasta.png"

const boton = document.getElementById("btn");
const menu = document.querySelector(".menu");
const precio = document.querySelector(".precio");
const imagen = document.querySelector(".imagen");
const imgCafe = document.getElementById("imgCafe");
const descripcion = document.querySelector(".descripcion");
let contador = 1;

boton.addEventListener("click", () => {

    if (contador == 0) {
        boton.classList.replace("boton_segundoClic", "boton_inicial");
        precio.textContent = "$3";
        imgCafe.src = "https://www.html6.es/img/cafe1.png";
        descripcion.textContent = "Cafe Colombia";

        menu.removeChild(menu.lastElementChild);

        contador++;
    }
    else if (contador == 1) {
        boton.classList.replace("boton_inicial", "boton_primerClic");
        precio.textContent = "$5";
        imgCafe.src = "https://www.html6.es/img/cafe2.png";
        descripcion.textContent = "Mucho Cafe";

        contador++;
    }
    else {
        boton.classList.replace("boton_primerClic", "boton_segundoClic");
        precio.textContent = "$15";
        descripcion.textContent = "Desayuno Completo";

        const divMagdalena = document.createElement("div");
        divMagdalena.classList.add("imagen");
        divMagdalena.appendChild(magdalena);

        menu.appendChild(divMagdalena);

        contador = 0;
    }
})
