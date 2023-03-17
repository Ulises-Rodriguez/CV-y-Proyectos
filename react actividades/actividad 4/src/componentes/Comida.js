import React from "react";
import estrella from '../assets/estrella.png';

const Comida = ({ productos,
    setProductos,
    misProductos,
    setMisProductos
    }) => {

    const añadir = (id, nombre) => {
        setMisProductos([...misProductos, {
            producto: nombre,
            estrellas: 0
        }]);

        setProductos(items=> items.map(item=>{
            if (id === item.id) {
                //The properties are added in order, so if you want to override existing properties, you need to put them at the end instead of at the beginning:
                return {...item, estado:true};
            }
            return item;
        }));
    }

    const crearElementos = () => {
        return productos.filter(producto=> producto.estado === false).map((comida, index) => (
            <div className="comida" key={index} onClick={() => añadir(comida.id, comida.producto)}>{comida["producto"]}</div>
        ))
    }

    const incrementarEstrellas = (e)=>{
   
        let parent = e.target.parentNode;
        // console.log(e.target.parentNode)
        // console.log(e.target)
        if (parent.children.length <= 5) {

            const divEstrellas = document.createElement("div");
            divEstrellas.className = "divEstrellas";
            divEstrellas.style.display = "inline";

            const imgEstrella = document.createElement("img");
            imgEstrella.src = estrella;

            divEstrellas.appendChild(imgEstrella);

            parent.appendChild(divEstrellas);

        }else{
            // console.log(e.target.parentNode.children)
            // console.log(e.target.parentNode.children.length)
            // console.log(e.target.parentNode)
            // console.log(e.target)

            while (parent.children.length !== 1) {
                e.target.nextElementSibling.remove();
            }    
        }

        // console.log(e.target.parentNode.children)

    }

    // let lasEstrellas = [];

    // const counstruirEstrellas = (cantidad)=>{
    //     lasEstrellas = [];

    //     for (let i = 0; i < cantidad; i++) {
    //         lasEstrellas.push(<img key={i} src={estrella} alt=""></img>)
    //     }

    //     return lasEstrellas;
    // }

    // const incrementar = (nombre,cuantas)=>{
    //     setMisProductos(prevItems=>
    //         prevItems.map(item=>{
    //             if (item.producto === nombre) {
    //                 return {...item,estrellas : cuantas + 1}
    //             }

    //             return item;
    //         })
    //     )
    // }

    return (
        <>
            <div className="menu">
                {crearElementos()}
            </div>
            {misProductos.map((item) => (
                <div className="menuElegido" key={item.producto} >
                    <div className="comidaMenuElegido" onClick={incrementarEstrellas}>
                        {item.producto}
                    </div>
                </div>
            ))}
            {/* jab solucion */}
            {/* {misProductos.map((dato) => (
                <div className="cuadro" key={dato.producto} >
                    <div className="comidaMenuElegido" onClick={()=>incrementar(dato.nombre,dato.estrellas)}>
                        {dato.producto}
                    </div>
                    <div>
                        {counstruirEstrellas(dato.estrella)}
                    </div>
                </div>
            ))} */}
        </>
    );
};

export default Comida;
