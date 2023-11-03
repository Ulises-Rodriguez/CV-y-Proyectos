//estos 2 serian lo mismo
// import calculadora from './calculadora.js';
const calculadora = require('./calculadora.js');

//para usar la primera tendrias q agregar al html en el script o packaje.json type="module"

const c = console.log; //en esta variable guardamos el metodo console.log --> entonces en ves de hacer console.log() hacemos c()

c(calculadora.sumar(2,5));
c(calculadora.restar(2,5));
c(calculadora.multiplicar(2,5));
c(calculadora.dividir(4,2));