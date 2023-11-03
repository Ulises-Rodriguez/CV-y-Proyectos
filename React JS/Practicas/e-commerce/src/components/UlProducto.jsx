import React from 'react'

export const UlProducto = ({producto}) => {

    const {name,precio,cantidad} = producto;

    return (
        <ul className='ulResumenCompra ulProductos'>
            <li>{name}</li>
            <li>{cantidad}</li>
            <li>${precio}</li>
            <li>${precio * cantidad}</li>
        </ul>
    )
}
