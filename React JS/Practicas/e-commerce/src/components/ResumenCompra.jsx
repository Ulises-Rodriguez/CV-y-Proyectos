import React, { useContext } from 'react'
import { Context } from '../context/Context';
import { UlProducto } from './UlProducto';

export const ResumenCompra = () => {
    const { cart } = useContext(Context);


    return (
        <div className='container-fluid'>
            <div className='resumenTitulo'>
                Resumen de compra
            </div>
            <div>
                <div className='resumenContainer'>
                    <ul className='ulResumenCompra'>
                        <li>
                            Producto
                        </li>
                        <li>
                            Cantidad
                        </li>
                        <li>
                            Precio Unitario
                        </li>
                        <li>
                            Precio Total
                        </li>
                    </ul>
                    {cart["productos"].map(producto => <UlProducto key={producto.name} producto={producto} />)}
                </div>
                <div className='container-fluid precioTotal'>
                    <p>Precio Total_________${Math.round(cart["precioTotal"] * 100) / 100}</p>
                </div>
            </div>
        </div>
    )
}
