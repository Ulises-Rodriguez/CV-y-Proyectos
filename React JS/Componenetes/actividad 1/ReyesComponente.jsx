import React from 'react'
import '../actividad 1/reyesCss.css'

function ReyesComponente(props) {
    
    const comprado = (elemnto)=>{
        props.setTotalPago((e)=>e + props.precio); //si pones {} en la funcion flecha no va andar, lo mismo si pones ; y si queres agregar otra intruccion ponele , despues del props.precio
        elemnto.target.parentNode.style.display = "none";
    }

    return (
        <div className='reyConatiner' style={{backgroundColor : props.color}}> 
            <div className='reyNombre'>{props.rey}</div>
            <img src={props.img}/>
            <p className='precio'>Precio = ${props.precio}</p>
            <button onClick={comprado}>Comprar</button>
        </div>
    )
}

export default ReyesComponente