const container = document.querySelector(".botonesContainer");
const divImg = document.querySelector(".imgContainer");
const img = document.querySelector(".tinoImg");

//eventos de los botones
const botonesEventos = (boton1,boton2,boton3)=>{
    boton1.addEventListener("click",()=>{
        //ocultar boton1
        boton1.style.visibility = "hidden";

        //cambios img
        img.style.borderRadius = "8px";
        img.style.border = "solid 2px #000";
        img.style.opacity = "0.5";
        img.style.transform = "rotate(15deg)";
    });

    boton2.addEventListener("click", () => {     
        
        //mostrar la img o ocultarla
        if (img.style.visibility == "hidden") {
            boton2.style.backgroundColor = null;
            img.style.visibility = "visible";
        }
        else {
            boton2.style.backgroundColor = "rgb(241, 219, 145)";
            img.style.visibility = "hidden";
        }
    });

    boton3.addEventListener("click", () => {
        //restablecer los botones
        boton1.style.visibility = "visible";
        boton2.style.backgroundColor = "#fff";
        img.style.visibility = "visible";
        img.style.borderRadius = null;
        img.style.border = null;
        img.style.opacity = null;
        img.style.transform = null;
    });
};

const crearBotones = ()=>{
    //creo botones
    const botonOculta = document.createElement("button");
    const botonImg = document.createElement("button");
    const botonRestablecer = document.createElement("button");

    botonOculta.textContent = "Boton 1";
    botonImg.textContent = "Boton 2";
    botonRestablecer.textContent = "Boton 3";

    //estilo
    botonOculta.style.color = "#48e";
    botonImg.style.color = "#48e";
    botonRestablecer.style.color = "#48e";

    botonOculta.style.fontSize = "20px";
    botonImg.style.fontSize = "20px";
    botonRestablecer.style.fontSize = "20px";

    //indico nodo padre
    container.appendChild(botonOculta);
    container.appendChild(botonImg);
    container.appendChild(botonRestablecer);

    botonesEventos(botonOculta,botonImg,botonRestablecer);


    //otra forma de hacerlo seria con insertAdjacentElement
    // container.insertAdjacentElement("beforeend",`
    // <button class="boton1" value="1">Boton 1</button>
    // <button class="boton2" value="2">Boton 2</button>
    // <button class="boton3" value="3">Boton 3</button>`)
    //esto te crea y agrega los elementos
};


crearBotones();