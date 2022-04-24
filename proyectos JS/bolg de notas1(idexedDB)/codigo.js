//primero creo la solicictud, osea la base de datos donde guardo la info

// const requestIDB = indexedDB.open("notasbase",1); //aca abrimos "notasbase" en caso de q ya exista o la creamos en caso de q no existas
// //DATO: si el nombre q le quisiera poner a la variable fuera indexedDB entonces en el lado der del = tendria q poner windows.indexedDB

// requestIDB.addEventListener("upgradeneeded",()=>{
//     let db = requestIDB.result;
//     db.createObjectStore("notas",{
//         autoIncrement : true //para ir incrementado el key
//     })
// });

// requestIDB.addEventListener("success",()=>{
//     console.log("todo bien");
// });

// requestIDB.addEventListener("error",()=>{
//     console.log("la base de datos no se puede cargar correctamente");
// });

// // vamos a añadir los objetos o notas
// const añadirObjeto = objeto=>{
//     const db = IDBRequest.result;
//     const transactionIDB = db.transaction("notas","readwrite");
//     const objectStore = transactionIDB.objectStore("notas");
//     objectStore.add(objeto);
//     transactionIDB.addEventListener("complete",()=>{
//         console.log("objeto gregado correctamente");
//     })
// }


// const leerObjetos = ()=>{
//     const db = IDBRequest.result;
//     const IDBTransaction = db.transaction("notas","readonly");
// }

// creamos los elementos de forma dinamica
const crearDinamicamente = (key,nota)=>{
    const notaContainer = document.createElement("div");
    const h2 = document.createElement("h2");
    const opciones = document.createElement("div");
    const guardarCambio = document.createElement("button");
    const borrar = document.createElement("button");

    //clases de los elementos
    notaContainer.classList.add("nota");
    opciones.classList.add("opciones");
    guardarCambio.classList.add("no-permitido");
    borrar.classList.add("eliminar");

    //texto dentro de los elementos
    h2.textContent = nota.nombre;
    guardarCambio.textContent = "Guardar Cambios";
    borrar.textContent = "Borrar";

    //atributos para modificar el h2
    h2.setAttribute("contenteditable","true");
    h2.setAttribute("spellcheck","false");

    //meto cada elemento dentro de su container
    opciones.appendChild(guardarCambio);
    opciones.appendChild(borrar);
    notaContainer.appendChild(h2);
    notaContainer.appendChild(opciones);

    //tengo q habilitar el boton de cambio
    h2.addEventListener("keyup",()=>{
        guardarCambio.classList.replace("no-permitido","permitido");
    });

    guardarCambio.addEventListener("click",()=>{
        if (guardarCambio.className == "permitido") {
            modificarNota(key,{nombre : h2.textContent});
            guardarCambio.classList.replace("permitido","no-permitido");
        }
    });

    borrar.addEventListener("click",()=>{
        borrarNota(key);
        document.getElementById(".notas").removeChild(notaContainer);
    });

    return notaContainer;
};