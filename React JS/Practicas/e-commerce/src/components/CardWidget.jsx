import React from 'react';
import { CarritoImg } from './CarritoImg';
import { CantidadProductos } from './CantidadProductos';
import { CarritoLi } from './CarritoLi';
import { Precio } from './Precio';
import { useContext } from 'react';
import { Context } from '../context/Context';
import { BtnOpcionesCompra } from './BtnOpcionesCompra';

export const CardWidget = () => {

    const { cart } = useContext(Context);

    return (
        <>
            <div className="btn-group dropstart">
                <button type="button" className="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                    <CantidadProductos />
                    <CarritoImg />
                </button>
                <ul className="dropdown-menu ulCarrito">
                    {cart["productos"].map(producto => <CarritoLi key={producto.id} nombreProducto={producto.name} cantidad={producto.cantidad}/>)}
                    <li>
                        <ul className='ulComprar'>
                            <Precio />
                            <li>
                                <BtnOpcionesCompra opcion={"Comprar"}/>
                                <BtnOpcionesCompra opcion={"Reset"}/>
                            </li>
                        </ul>
                    </li>
                </ul>
            </div>
        </>
    )
}
