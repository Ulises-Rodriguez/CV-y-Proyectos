const fotos = document.getElementById("fotos");

fotos.addEventListener("change",()=>{
    cargarFoto(fotos.files);//esto de aca es un array

});

const cargarFoto = img=>{
    for (let i = 0; i < img.length; i++) { //el for para poder ir recorriendo el array de fotos q le paso
        const reader = new FileReader();
        if (img) { //compruebo q el array no este vacio
            reader.readAsDataURL(img[i]);
            reader.addEventListener("load",e=>{ //cuando se dispare el evento de carga
                let newimg = `<img src='${e.currentTarget.result}' class='imagenDeGaleria'>`; //creamos la imagen y añado la clase "imagenDeGaleria" para cada foto (esto para poder seleccionar la foto q quiera y expandirla abajo)
                //otra forma seria crear un elemento img y despues ir añadiendo los atributos
                document.querySelector(".galeria").innerHTML += newimg; //y la añadimos dentro del "div" galeria (creo q tambien se podria hacer con createElement y despues añadirlo con appendchild)
            })
        }
    }
}