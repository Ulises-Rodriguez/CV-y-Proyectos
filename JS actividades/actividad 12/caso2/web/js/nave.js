window.onload=inicio;
let nave;

function inicio(){
    nave=document.querySelector("#nave");
    
    let altura = window.innerHeight;
    let alto = nave.offsetLeft;
    let alturaNave = nave.offsetHeight;

    let objeto = window.getComputedStyle(document.querySelector("body"));
    let propiedadBorde = parseInt(objeto.borderBottomWidth);

    let calculo = altura - alto - alturaNave - propiedadBorde;

    console.log(calculo);

    // console.log("left: "+____);
    // console.log("top: "+____);    
    // console.log("bottom: "+_____);
    // console.log("altura de la nave: "+____);
}