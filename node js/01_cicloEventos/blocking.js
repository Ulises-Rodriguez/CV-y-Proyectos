const fs = require('fs'); //fs es un modulo de JS q nos permite leer archivos

console.log("inicio del programa");

const data = fs.readFileSync("archivo.txt","utf8"); //lee el archivo de forma sincrona

console.log(data);

console.log("fin del programa");

//fijate q al ser bloqueante todo se ejecuta y se muestra en consola como en orden lineal 