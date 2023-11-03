const sumar = (a,b)=>{
    return a+b;
}

const restar = (a,b) => a-b;

const multiplicar = (a,b) => a*b;

const dividir = (a,b) => a/b;

const calculadora = {
    sumar : sumar,
    restar, //recorda q si lo q asignas tiene el mismo nombre para clave y valor no hace falta escribir clave : valor 
    multiplicar,
    dividir
}

// export default calculadora;
module.exports = calculadora;