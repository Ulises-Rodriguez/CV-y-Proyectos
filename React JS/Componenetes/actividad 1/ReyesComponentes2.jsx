import React from 'react'
import '../actividad 1/reyesCss.css'

function ReyesComponente(props) {

    const ruta = "https://www.html6.es/img/rey_";
    const imagen = `${ruta}${props.rey.toLowerCase()}.png`; //esto en ves de mandarselo como parametro en el componente padre

    const comprado = (elemnto) => {
        props.setTotalPago((e) =>
            e + props.precio
        );
        elemnto.target.parentNode.style.display = "none";
        //en el curso ponene muchas veces elemnto.target.parentNode.parentNode.parentNode.style.display = "none"; por como creo los elementos de del return de abajo
    }

    return (
        <div className='reyConatiner' style={{ backgroundColor: props.color }}>
            <div className='reyNombre'>{props.rey}</div>
            <img src={imagen} />
            <p className='precio'>Precio = ${props.precio}</p>
            <button onClick={comprado}>Comprar</button>
        </div>
    )
}

export default ReyesComponente