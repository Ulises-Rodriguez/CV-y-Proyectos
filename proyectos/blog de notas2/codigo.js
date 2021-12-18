//crear elementos de forma dinamica
const buttonAdd = document.getElementById("añadir");

buttonAdd.addEventListener("click",()=>{
    // let inputText = document.querySelector(".input-nota").textContent;
    crearElement();
});

const crearElement = ()=>{
    //creo los elementos
    const notaContainer = document.createElement("div");
    const h2 = document.createElement("h2");
    const opcionesContainer = document.createElement("div");
    const completeButton = document.createElement("button");
    const noCompleteButton = document.createElement("button");
    const deleteButton = document.createElement("button");

    //les doy sus clases
    notaContainer.classList.add("nota");
    opcionesContainer.classList.add("opciones");

    //le doy los atributos al h2 para poder modificarlo
    h2.setAttribute("contenteditable","true");
    h2.setAttribute("spellcheck","false");

    //les doy el texto q contiene
    // h2.textContent = inputText;
    completeButton.textContent = "Completado";
    noCompleteButton.textContent = "No Completado";
    deleteButton.textContent = "Borrar";

    //meto cada atributo dentro de su contenedor
        //los botones dentro del div con la clase "opciones"
    opcionesContainer.appendChild(completeButton);
    opcionesContainer.appendChild(noCompleteButton);
    opcionesContainer.appendChild(deleteButton);
        //h2 y opciones dentro del div con la clase "nota"
    notaContainer.appendChild(h2);
    notaContainer.appendChild(opcionesContainer);
        //por ultimo todo lo anterior dentro del div con el id "notas"
    const notas = document.getElementById("notas");
    notas.appendChild(notaContainer);

    //ahora añado eventos para q cambie de color los botones o borrar la nota 
    completeButton.addEventListener("click",()=>{
        completeButton.style.color = "#0f0";
    });

    completeButton.addEventListener("dblclick",()=>{
        completeButton.style.color = "#000";
    });

    noCompleteButton.addEventListener("click",()=>{
        noCompleteButton.style.color = "#f00";
    });

    noCompleteButton.addEventListener("dblclick",()=>{
        noCompleteButton.style.color = "#000";
    });

    deleteButton.addEventListener("click",()=>{
        notas.removeChild(notaContainer);
    });

    // return notaContainer;
}