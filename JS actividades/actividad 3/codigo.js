const inputNombre = document.querySelector(".inputNombre");
const botonSaludar = document.querySelector(".botonSaludar");
const botonBorrar = document.querySelector(".botonBorrar");
const divSaludo = document.querySelector(".textoContainer");

botonBorrar.addEventListener("click",()=>{
    inputNombre.value = "";
    inputNombre.focus();
    divSaludo.textContent = "";
});

botonSaludar.addEventListener("click",()=>{
    const nombre = inputNombre.value;
    const nombreFromateado = nombre.substring(0,1).toUpperCase() + nombre.substring(1).toLowerCase();
    const saludo = `Hola ${nombreFromateado}, como estas?`;

    divSaludo.textContent = saludo;
});

