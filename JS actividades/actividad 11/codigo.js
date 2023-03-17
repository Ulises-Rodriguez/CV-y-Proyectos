window.onload = inicio;
const body = document.body;
// const reyes = ["atanagildo", "ataulfo", "ervigio", "leogivildo", "recesvinto", "sisebuto", "teodorico"];
const reyes = [
{
    rey : "atanagildo",
    precio : "$82",
},{
    rey : "ataulfo",
    precio : "$65",
},{
    rey : "ervigio",
    precio : "$86",
},{
    rey : "leogivildo",
    precio : "$75",
},{
    rey : "recesvinto",
    precio : "$80",
},{
    rey : "sisebuto",
    precio : "$71",
},{
    rey : "teodorico",
    precio : "$" + Math.floor(Math.random()*100),
}];



let orden2 = []
//metodo 1
const ordenar = ()=>{
    let orden1 = reyes.map((valor,indice)=>indice);
    
    while (orden1.length > 0) {
        let azar = Math.floor(Math.random() * orden1.length);
        
        orden2.push(orden1[azar]);
    
        orden1.splice(azar,1);
    }

    console.log(orden2)
}

const crearElementos = ()=>{
    const divContenedor = document.createElement("div"); 
    const divPrecio = document.createElement("div");
    const divContenedorReyes = document.createElement("div");

    //agreguemos las clases
    divPrecio.className = "precio";
    divContenedorReyes.className = "contenedorReyes";

    //agrego elementos dentro de divPrecio
    const divInfo = document.createElement("div");
    divInfo.className = "divInfo";

    const precioBoton = document.createElement("button");
    precioBoton.className = "precioBoton";
    precioBoton.textContent = "X";

    precioBoton.addEventListener("click",()=>{
        divPrecio.style.visibility = "hidden";
    });

    const bInfo = document.createElement("b");
    const imgInfo = document.createElement("img");

    divInfo.appendChild(bInfo);
    divInfo.appendChild(imgInfo);

    divPrecio.appendChild(precioBoton);
    divPrecio.appendChild(divInfo);

    let fragmento = new DocumentFragment();
    // let fragmento = document.createDocumentFragment()

    for (let i = 0; i < orden2.length; i++) {
        const div = document.createElement("div");
        div.id = i;

        const imgRey = document.createElement("img");
        imgRey.src = `img/rey_${reyes[orden2[i]].rey}.png`;
        imgRey.id = `${reyes[orden2[i]].rey}`;
        imgRey.className = `${reyes[orden2[i]].precio}`;

        imgRey.addEventListener("click",(e)=>{
            // console.log(e)
            // let nombre = e.target.id.substring(0,1).toUpperCase() + e.target.id.substring(1).toLowerCase();
            // let precio = e.target.className;
            let nombre = reyes[orden2[i]].rey.substring(0,1).toUpperCase() + reyes[orden2[i]].rey.substring(1).toLowerCase();
            let precio = reyes[orden2[i]].precio;
            bInfo.textContent = `Has reservado una cena con ${nombre} ${precio}`;
            imgInfo.src = `img/rey_${reyes[orden2[i]].rey}.png`;
            imgInfo.style.marginLeft = "auto";
            imgInfo.style.marginRight = "auto";
            divPrecio.style.visibility = "visible";
        });

        const bRey = document.createElement("b");
        bRey.textContent = reyes[orden2[i]].rey.substring(0,1).toUpperCase() + reyes[orden2[i]].rey.substring(1).toLowerCase();


        div.appendChild(imgRey);
        div.appendChild(bRey);


        fragmento.appendChild(div);
    };

    divContenedorReyes.appendChild(fragmento);

    divContenedor.appendChild(divPrecio);
    divContenedor.appendChild(divContenedorReyes);

    body.appendChild(divContenedor);

};

function inicio(){
    ordenar();
    crearElementos();
};