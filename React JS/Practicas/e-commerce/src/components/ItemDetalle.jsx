import React, { useState } from 'react'
import { Counter } from './Counter'
import { BtnAñadir } from './BtnAñadir';

export const ItemDetalle = ({producto,children}) => {

    const {name,precio,stock,descripcion} = producto;

    const [cantidad, setCantidad] = useState(0);

    return (
        <>
            <div className='productoDetalleContainer'>
                <div>
                    {children}
                </div>
                <div>
                    <p className='tituloProductoDetalle'>nombre: {name}</p>
                    <p>detalles: {descripcion}</p>
                    <p className='precioProductoDetalle'>${precio}</p>
                    <p>stock: {stock}</p>
                    <div>
                        <Counter stock={stock} setCantidad={setCantidad}/>
                        <BtnAñadir nombre={name} precio={precio} cantidad={cantidad}/>
                    </div>
                </div>
            </div>
        </>
    )
}
