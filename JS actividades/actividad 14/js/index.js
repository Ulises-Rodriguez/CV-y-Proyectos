const comidas = document.querySelector(".comidas");
const infoProducto = document.querySelector(".infoProducto");
const menuElegidoContainer = document.querySelector(".menuElegidoContainer");
const menuElegido = document.querySelector(".menuElegido");
const infoContainer = document.querySelector(".infoContainer");
const ponerDinero = document.querySelector(".ponerDinero");
const dineroTotal = document.querySelector(".dinero");
const menuElegidoInfo = document.querySelector(".menuElegidoInfo");
const cuenta = document.querySelector(".cuenta");
const total = document.querySelector(".total");

const cargarDinero = (e)=>{

    ponerDinero.addEventListener("change",e=>{
        dineroTotal.textContent = `$${e.target.value}`;
        infoContainer.removeChild(ponerDinero);
    });
}

const presupuesto = (precio)=>{
    dinero = Number(dineroTotal.textContent.slice(1));

    if (dinero >= precio) {
        dinero -= Number(precio); 
        dineroTotal.textContent = `$${dinero}`;

        return true;
    }else{
        alert("Presupuesto insuficiente");
    }
}

const aPagar = (nombre,precio)=>{
    const divComida = document.createElement("div");
    divComida.classList.add("comidaInfo");
    divComida.textContent = `${nombre}_____$${precio}`;

    menuElegidoInfo.appendChild(divComida);

    total.textContent = Number(Number(precio) + Number(total.textContent));

    cuenta.style.visibility = "visible";
}

const imgEvento = (img,nombre,precio)=>{

    // let nombre = arr[comida]["nombre"];
    // let precio = arr[comida]["precio"];

    img.addEventListener('mouseover',()=>{
        infoProducto.textContent = `${nombre} $(${precio})`; 
    });

    img.addEventListener('mouseout',()=>{
        infoProducto.textContent = "";
    });

    img.addEventListener('click',()=>{
        aux = presupuesto(precio);
        menuElegidoContainer.style.visibility = "visible";
        
        if (aux) {
            //f the given child is a reference to an existing node in the document, appendChild() moves it from its current position to the new position — there is no requirement to remove the node from its parent node before appending it to some other node. This means that a node can't be in two points of the document simultaneously. The Node.cloneNode() method can be used to make a copy of the node before appending it under the new parent. Copies made with cloneNode are not automatically kept in sync.
            menuElegido.appendChild(img);

            aPagar(nombre,precio);
        }

    });
}


const mostrarMenu = (arr)=>{

    //jab solucion
    // PRODUCTOS.filter(valor => valor.disponible === true).map(valor=>
    //     document.querySelector(".comidas").insertAdjacentHTML("beforeend",
    //     `<img src="./img/${valor.imagen}" onmouseover="conocer(this)" onmouseout="limpiar()" onclick="comprar(this)" alt="${valor.nombre}">`
    //     )
    // )

    //el this es para indicarle a q elemento se hace referencia (es como el event.target)

    const fragmento = document.createDocumentFragment();

    //forma de hacerlo con map
    arr.map(comida=>{

        let imgComida = document.createElement("img");
        imgComida.src = `./img/${comida.imagen}`;
        imgComida.alt = `${comida.nombre}`;
    
        imgEvento(imgComida,comida.nombre,comida.precio); 

        fragmento.appendChild(imgComida)
    })

    // for (let comida = 0; comida < arr.length; comida++) {
    //     const imgComida = document.createElement("img");
    //     imgComida.src = `./img/${arr[comida]["imagen"]}`;
    //     imgComida.alt = `${arr[comida]["nombre"]}`;
    
    //     imgEvento(imgComida,comida,arr);

    //     fragmento.appendChild(imgComida);
    // }

    comidas.appendChild(fragmento);

    return comidas;
}

mostrarMenu(PRODUCTOS);
cargarDinero();
