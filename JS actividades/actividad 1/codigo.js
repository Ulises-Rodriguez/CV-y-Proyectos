const boton1 = document.querySelector(".boton1");
const boton2 = document.querySelector(".boton2");
const boton3 = document.querySelector(".boton3");
const boton4 = document.querySelector(".boton4");

const divTexto = document.querySelector(".texto");

const img = new Image();
img.src = "tino.png";

const almacenTexto = (numBoton)=>{
    num = Number(numBoton);

    if (num == 1) {
        divTexto.textContent = "Hola Mundo";
    }
    else if (num == 2) {
        divTexto.appendChild(img);
    }
    else if (num == 3) {
        const newBoton = document.createElement("button");
        newBoton.textContent = "Boton";

        divTexto.appendChild(newBoton);
    }
    else {
        divTexto.innerHTML = " ";
    }
};

boton1.addEventListener("click",()=>{
    divTexto.textContent = " ";
    almacenTexto(boton1.value);
});

boton2.addEventListener("click", () => {
    divTexto.textContent = " ";
    almacenTexto(boton2.value);
});

boton3.addEventListener("click", () => {
    almacenTexto(boton3.value);
});

boton4.addEventListener("click", () => {
    almacenTexto(boton4.value);
});