const fs = require('fs');

console.log("inicio del programa");

//JS por defecto es no bloqueante
fs.readFile("archivo.txt","utf8",(err,data)=>{  //(err,data)=>{...} es una callback (funcion q se pasa como argumento de otra funcion q se ejecuta dentro de esta) codigo q se ejecuta asincronamente o en segundo plano
//callbakc --> funcion q se le pasa a otra funcion como argumento y q se ejecuta despues de q se haya ejecutado otra operacion
//no tiene xq ser asincrono
    if (err) {
        throw err;
    }

    console.log(data);
})

console.log("fin del programa");

//al ser no bloqueante se ejecutan primero los console.log "inicio del programa" "fin del programa"
//ya q la peticion de leer el archivo se pone en la pila de peticiones se resulve ahi y luego se lo pone en la pila principal
//mientras eso pasa se ejecuta el resto del programa



//CALLBACK
//casi todo en JS recive un callbakc
//array.map(nombres=>console.log(nombre)) --> la funcion es (nombres=>console.log(nombre)) q se ejecuta luego de q se accede a los elementos del array

//tambien podrias llamarlo asi con map,filter,reduce,etc
// const nombreSaludo = (nombre)=>{
//     console.log(nombre);
// }

// ["tino","pepe","Juan"].map(nombreSaludo);


//btn.addEventListener("click",()=>{consolo.log("me diste click")}) --> la funcion es ()=>{consolo.log("me diste click")} q se ejecuta luego de q se da click al btn


// const agregar = (arr,callback)=>{
//     arr.push("jkl");

//     callback();
// }

// console.log(agregar(["tino","juan","pepe"],()=>{
//     console.log("terminamos");
// }))


//esto lo podes ver tambien como

// const fun = ()=>{
//     console.log("terminamos");
// })

// const agregar = (arr,callback)=>{
//     arr.push("jkl");

//     callback();
// }

// console.log(agregar(["tino","juan","pepe"],fun)


//la callback tambien puede recivier argumentos
//let arr = ["tino","juan","pepe"];

// const agregar = (arr,callback)=>{
//     arr.push("jkl");

//     callback(arr);
// }

// console.log(agregar(arr,(arr)=>{
//     console.log(arr.length);
// }))