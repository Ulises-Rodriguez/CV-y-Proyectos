window.onload = inicio;
let reyes = ["atanagildo", "ataulfo", "ervigio", "leogivildo", "recesvinto", "sisebuto", "teodorico"];
let camisetas = ["camisetaNegra.png", "camisetaBlanca.png"];
let camisetaActual = 0;
let reyNombre = Math.floor(Math.random() * reyes.length);
const texto = document.querySelector(".texto");
const camiseta = document.querySelector(".camiseta");
let tamaño = 2;
const imprimirBoton = document.getElementById("imprimir");


// Escribir el resto del código JavaScript aquí.
// Intenta no modificar los arrays superiores ni crear nuevos manualmente (no es necesario).
// A continuación he añadido algunas funciones interesantes por si las necesitas.

const formatearNombre = ()=>{
	return (reyes[reyNombre].substring(0,1).toUpperCase() + reyes[reyNombre].substring(1).toLowerCase());
}

const insertarCamiseta = ()=>{
	//creo la img de la camiseta
	camiseta.insertAdjacentHTML("beforeend", `<img id="#dibujo" src='img/${camisetas[camisetaActual]}'>`);
	//evento q cambia el color de la camiseta al hacer click
	const img = document.getElementById("#dibujo");
	img.addEventListener("click", () => {
		//con esto te ahorras el if else ya q los valores booleanos son 0(false) 1(true)
		camisetaActual = Number(!camisetaActual);
		img.src = `img/${camisetas[camisetaActual]}`;
	});
};

const insertarTexto = ()=>{
	let nombreFormateado = formatearNombre();
	texto.textContent = `yo ♡ ${nombreFormateado}`;
	
	camiseta.addEventListener("click",()=>{
		if (camisetaActual == 1) {
			texto.style.color = "#000";
		}else{
			texto.style.color = "#fff";
		}
	});
};

const insertarRey = ()=>{
	const imagen = document.querySelector(".imagen");

	const reyImg = document.createElement("img");
	reyImg.src = `img/rey_${reyes[reyNombre]}.png`;
	reyImg.id = "#rey";

	imagen.appendChild(reyImg);

	document.getElementById("#rey").addEventListener("click",()=>{
	
		if (reyes.length-1 > reyNombre) {
			reyNombre = reyNombre + 1;
			reyImg.src = `img/rey_${reyes[reyNombre]}.png`;
			texto.textContent = `yo ♡ ${formatearNombre()}`;
		} else {
			reyNombre = 0;
			reyImg.src = `img/rey_${reyes[reyNombre]}.png`;
			texto.textContent = `yo ♡ ${formatearNombre()}`;
		}
	});
};

const teclado = ()=>{
	window.addEventListener("keydown",(e)=>{

		let codigo = e.key;
		let textoLimite = document.querySelector(".texto").innerHTML.length;
		let excepciones = ["Delete","Backspace","+","-","ArrowUp","ArrowDown","ArrowLeft","ArrowRigth"];

		if (textoLimite >= 35 && excepciones.indexOf(e.key) == -1) {
			e.preventDefault()	
		}else{
			if (codigo == "+") {
				//xq crear otro if y no ponerlo dentro del primero? --> xq sino no te funciona el prevenDefault
				if (tamaño <=3) {
					tamaño += .1;
				}
				e.preventDefault();
			}else if (codigo == "-") {
				if (tamaño >= 1) {
					tamaño -= .1;
				}
				e.preventDefault();
			}
	
			texto.style.fontSize = tamaño + "em";
		}

	});
};

function inicio() {
	// Eventos y acciones iniciales
	insertarCamiseta();
	insertarRey();
	insertarTexto();
	teclado();
	imprimirBoton.addEventListener("click",()=>{
		imprimir();
	});
}

function imprimir() {
	// Imprime lo que haya en pantalla en ese momento. Si sólo se desea que imprima unos elementos y no otros o personalizar lo que se envía a la impresora, se debería utilizar en conjunción con mediaqueries (@media print) de CSS.
	window.print();
}

