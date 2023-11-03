//mira la extension de los archivos

//esta es la forma q deberias trabajar
import { calculadora } from "./calculadora.mjs";

const c = console.log;

c(calculadora.sumar(2,5));
c(calculadora.restar(2,5));
c(calculadora.multiplicar(2,5));
c(calculadora.dividir(4,2));

//tabajar de esta manera tiene algunos requisitos mas
//Warning: To load an ES module, set "type": "module" in the package.json or use the .mjs extension

//solucion:

//1_el package.json es el archivo principal de confirguracion en node

//2_convertir los archivos de extension .js a mjs (module JS) --> fijate q si le cambias la extension el visual te hace los cambios en el import
    //tanto el archivo q mandas a llamar, como el archivo q se esta ejecutando tiene q tener la extension .mjs


//si bien la opcion 2_ es una opcion lo ideal es usar la 1_ (pero se ve mas adelante en el curso)