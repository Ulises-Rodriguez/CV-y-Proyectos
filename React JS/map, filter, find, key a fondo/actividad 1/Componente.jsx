import React from 'react'
import '../actividad 1/componenteCss.css'

function Componente({rey,reinado,vacas}) {

    const ruta = "https://www.html6.es/img/rey_";
    const imagen = `${ruta}${rey.toLowerCase()}.png`;

    return (
    <div className='reyConatiner'>
        <span className='reyNombre'>{rey.toUpperCase()}</span> ha comido {vacas} vacas en sus {reinado} años reinados
        <img src={imagen} />
    </div>
  )
}

export default Componente;