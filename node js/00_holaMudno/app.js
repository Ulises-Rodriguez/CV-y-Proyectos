let num1 = 5;
let num2 = 4;

let res = num1 + num2;

console.log(res); 

let saludo = "Hola mundo";

console.log(saludo);

//para ejecutar esto podes entrar a la carpeta q contine este archivo o le especificas la ruta
//node 00_HolaMundo/app.js o node app.js parado ya dentro de la carpeta


//en terminal:
    //procces te muestra la info del sigle thread de node
    //global seria como windows en el navegador pero para node (te muestra la info del procesos actual q se este ejecutando)


const sumar = (a,b)=>{
    return a+b;
}

console.log(sumar(10,5));


let edad = 25;

if (edad < 18) {
    console.log("sos menor de edad");
} else {
    console.log("sos mayor de edad");
}


//fijate q si tenes error la terminal tambien te tira donde esta el error, el tipo de error,etc