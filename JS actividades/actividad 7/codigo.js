window.onload = inicio;
function inicio() {
    agregarMonedasIniciales();
}

// Si quieres usar la mism imagen de la moneda de la actividad usa esta URL
let urlDeLaMoneda = "https://www.html6.es/img/moneda.png";

const numMonedas = document.querySelector(".numMonedas");
const monedas = document.querySelector(".monedas");
const inputCampo = document.getElementById("campo");
const btnJugar = document.querySelector(".boton");
const numsContenido = document.querySelector(".contenido");
const info = document.querySelector(".informacion");

//fucnion q crear las monedas iniciales
const agregarMonedasIniciales = () => {
    let fragmento = new DocumentFragment();

    for (let i = 0; i < 5; i++) {
        const imgMoneda = document.createElement("img");
        imgMoneda.src = urlDeLaMoneda;
        fragmento.appendChild(imgMoneda);
    }

    monedas.appendChild(fragmento);
}

//array donde guardo los numeros random
let arrayNumsRandom = [];

//funcion q crear los numeros random
const crearNumsRandom = (num) => {

    //creo un fragmento
    let fragmento = new DocumentFragment();

    //for para crear los numeros random
    for (let i = 0; i < num; i++) {

        let numRandom = Math.floor(Math.random() * (9 - 2) + 2);


        const divNumRandom = document.createElement("div");
        divNumRandom.classList.add("cuadro");
        divNumRandom.textContent = numRandom;

        //parte q se encarga de comparar a ver si los numeros coinciden
        if (Number(num) == numRandom) {
            divNumRandom.classList.add("verde");
        } else {
            divNumRandom.classList.add("rojo");
        }

        //añado los numeros al array (esto para pasarselo a la funcion q va a comparar los numeros random coinciden con el numero del usuario)
        arrayNumsRandom = [...arrayNumsRandom, numRandom];

        fragmento.appendChild(divNumRandom);
    }

    numsContenido.appendChild(fragmento);
}

let numAux = 0;
let contadorDeConicidencias = 0;

const masMonedas = (array, num) => {

    let fragmento = new DocumentFragment();

    for (let i = 0; i < array.length; i++) {
        if (num == array[i]) {
            contadorDeConicidencias += 1;

            numMonedas.textContent = Number(numMonedas.textContent) + 1;
            numAux = num;

            const imgMoneda = document.createElement("img");
            imgMoneda.src = urlDeLaMoneda;
            fragmento.appendChild(imgMoneda);
        }
    }
    monedas.appendChild(fragmento);

    info.textContent = `Se produjieron ${contadorDeConicidencias} y has ganado ${contadorDeConicidencias} monedas`;

    // const arrya2 = arrayNumsRandom.map((e) => {
    //     if (num == e) {
    //         numMonedas.textContent = Number(numMonedas.textContent) + 1;
    //         numAux = num;

    //         const imgMoneda = document.createElement("img");
    //         imgMoneda.src = urlDeLaMoneda;
    //         fragmento.appendChild(imgMoneda);
    //     }
    // })
    // monedas.appendChild(fragmento);
}

const menosMonedas = (array, num) => {

    for (let i = 0; i < array.length; i++) {


        if (monedas.children.length) {
            monedas.removeChild(monedas.lastChild);
        }
        if (num != array[i] && num != numAux) {
            numMonedas.textContent = Number(numMonedas.textContent) - Number(num);
            numAux = num;
            contadorDeConicidencias -= Number(num);
        }
    }

    if (contadorDeConicidencias <= 0) {
        info.textContent = `No se produjo ninguna coincidencia por lo que perdiste ${contadorDeConicidencias} monedas`;
    }
}

const vaciar = () => {
    inputCampo.value = "";
    inputCampo.focus();
}


btnJugar.addEventListener("click", () => {

    contadorDeConicidencias = 0;
    numsContenido.innerHTML = "";
    info.textContent = "";

    let numPlayer = inputCampo.value;

    if (numPlayer > 2 && numPlayer < 9) {
        crearNumsRandom(numPlayer);
        masMonedas(arrayNumsRandom, numPlayer);
        menosMonedas(arrayNumsRandom, numPlayer);
        vaciar();
    } else {
        inputCampo.value = "";
    }
});