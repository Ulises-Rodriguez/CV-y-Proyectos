// Math.floor(Math.random() * 5);
// document.querySelector(".inpuit").onkeydown
// if (e.key == "Enter") {

// }

const numRandom1 = document.querySelector(".num1");
const numRandom2 = document.querySelector(".num2");
const respuesta = document.querySelector(".respuesta");
const btnComprobar = document.querySelector(".btn");
const divRespuesta = document.querySelector(".textoRespuesta");
const divResultado = document.querySelector(".resultado");

numRandom1.value = Math.floor(Math.random() * 11);
numRandom2.value = Math.floor(Math.random() * 11);

const resolver = () => {
    const resultado = Number(numRandom1.value) + Number(numRandom2.value);
    divRespuesta.style.visibility = "visible";
    divResultado.style.visibility = "visible";

    if (respuesta.value == resultado) {
        divRespuesta.textContent = "Correcto";
        divRespuesta.style.color = "#0f0";

        divResultado.textContent = "";
    } else {
        divRespuesta.textContent = "Incorrecto";
        divRespuesta.style.color = "#f00";

        divResultado.textContent = `La respuesta de sumar ${numRandom1.value} + ${numRandom2.value} es ${resultado}`;
    }

    respuesta.value = "";
    respuesta.focus();
}

const newSum = () => {
    numRandom1.value = Math.floor(Math.random() * 11);
    numRandom2.value = Math.floor(Math.random() * 11);
}

btnComprobar.addEventListener("click", () => {
    resolver();
    newSum();
});


respuesta.addEventListener("keydown", (e) => {
    if (e.key == "Enter") {
        resolver();
        newSum();
    }
})
