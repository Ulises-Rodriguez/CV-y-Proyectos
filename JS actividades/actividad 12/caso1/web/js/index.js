window.onload=inicio;
let enlaces;

function inicio(){  
    enlaces=document.querySelector(".enlaces");
    document.querySelector(".burger").onclick=burger;
}
function burger(){  
  /* Es NECESARIO saber si ."enlaces" está visible o no (utilizando el valor de la propiedad 'display')*/

  // El objeto devuelto es del mismo tipo que el objeto devuelto por la propiedad style del elemento, sin embargo ambos objetos tienen un propósito distinto. El objeto devuelto por getComputedStyle es de sólo lectura y puede usarse para inspeccionar el estilo del elemento (incluyendo los estilos de una etiqueta <style> o una hoja de estlo). El objeto elt.style debería usarse para establecerel estilo de un elemento específico.
  let propiedades = window.getComputedStyle(enlaces)
  let propiedad = propiedades.display;
  console.log(propiedad)

  if (propiedad == "none") {
    enlaces.classList.add("mostrar");
    enlaces.classList.remove("ocultar");
  } else {
    enlaces.classList.add("ocultar");
    enlaces.classList.remove("mostrar");
  }
}

