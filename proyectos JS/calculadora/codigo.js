// window.onload = function(){ //Acciones tras cargar la página
//     pantalla = document.getElementById("pantalla"); //elemento pantalla de salida
// }

addEventListener("load",()=>{
    pantalla = document.getElementById("pantalla");
});

//------------------------------------------------------------------------------------------------------------------------

//funciones de operaciones(+,-,/,*,raiz,potencia)
const _sumar = (a,b)=>{
    let resultado = parseInt(a) + parseInt(b);
    return resultado;
};

const _restar = (a,b)=>{
    return a - b;
};

const _multiplicar = (a,b)=>{
    return a * b;
};

const _dividir = (a,b)=>{
    return a / b;
};

const _potencia = (a,b)=>{
    //capaz q Math.pow analiza todos esto casos (revisar xq a lo mejor los estoy dejando al pedo)
    let c;
    // if (b === 0 && a !== 0) {
    //     c = 1;
    //     return c; 
    // }
    // else if (a === 1) {
    //     return a;
    // }
    // else if (b === 1) {
    //     return a;
    // }
    // else if (b === -1 && a !== 0) {
    //     return 1 / a;
    // }
    // else{
    //     let aux = a;
    //     console.log("aux:" + aux);
    //     c = a;
    //     console.log("c: " + c);
    //     for (let i = 1; i < b; i++) {
    //         c = c * aux;    
    //         console.log("c nuevo:" + c);
    //     }
    //     return c;
    // }
    
    c = Math.pow(a,b);
    return c;
};

const _raiz = (a)=>{
    let c = Math.sqrt(a);
    return c;
};

const _log = (a)=>{
    let c = Math.log(a);
    return c;
};

//------------------------------------------------------------------------------------------------------------------------

//funcion borrar
const borrar = ()=>{
    pantalla.innerHTML = " ";
};

//------------------------------------------------------------------------------------------------------------------------

//aparecer numeros en pantalla
let x = "0";
let xi = 1;
let coma = 0;

//para futuro mirar si se puede trabajar con promesas
const numero = (num)=>{ //recoge el número pulsado en el argumento.
    if (x == "0" || xi == 1  ) { // inicializar un número, 
        pantalla.innerHTML = num; //mostrar en pantalla
        x = num; //guardar número
        if (num == ",") { //si escribimos una coma al principio del número
            pantalla.innerHTML = "0,"; //escribimos 0.
            x = num; //guardar número
            coma = 1; //cambiar estado de la coma
        }
    }
    else { //continuar escribiendo un número
        if (num == "," && coma == 0) { //si escribimos una coma decimal p�r primera vez
            pantalla.innerHTML += num;
            x += num;
            coma = 1; //cambiar el estado de la coma  
        }
        //si intentamos escribir una segunda coma decimal no realiza ninguna acción.
        else if (num == "," && coma == 1) {} 
        //Resto de casos: escribir un número del 0 al 9: 	 
        else {
            pantalla.innerHTML += num;
            x += num
        }
    }
    xi = 0 //el número está iniciado y podemos ampliarlo.
}

//------------------------------------------------------------------------------------------------------------------------

//Operadores

let num1;
let op;

const igual = ()=>{

    let num2 = parseInt(pantalla.textContent);
    let resultado;

    if (op == '+') {
        resultado = _sumar(num1,num2);
        pantalla.innerHTML = resultado;
    }
    else if (op == '-'){
        resultado = _restar(num1,num2);
        pantalla.innerHTML = resultado;
    }
    else if (op == '*'){
        resultado = _multiplicar(num1,num2);
        pantalla.innerHTML = resultado;
    }
    else if (op == '/'){
        resultado = _dividir(num1,num2);
        pantalla.innerHTML = resultado;
    }
    else if (op == 'x^y'){
        resultado = _potencia(num1, num2);
        pantalla.innerHTML = resultado;
    }
}

const seleccionarOperador = operador=>{

    num1 = parseInt(pantalla.textContent);
    op = operador;
    xi = 1;
};

const logaritmo = ()=>{
    let resultado;

    num1 = parseInt(pantalla.textContent);
    resultado = _log(num1);
    pantalla.innerHTML = resultado;
}

const raizCuadrada = ()=>{
    let resultado;

    num1 = parseInt(pantalla.textContent);
    resultado = _raiz(num1);
    pantalla.innerHTML = resultado;
}