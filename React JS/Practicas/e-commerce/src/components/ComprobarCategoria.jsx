import React from 'react'
import { ItemDetalle } from './ItemDetalle';
import { useParams } from 'react-router-dom';
import { NotFound } from '../pages/NotFound';

export const ComporbarCategoria = ({ producto }) => {
    const { consola, juego } = useParams();

    if (Object.keys(useParams()).length === 1) {

        return <>
            <div>
                {(producto !== undefined) ? <ItemDetalle producto={producto}>
                    <img className='imgProductosDetalle' src={producto.url} alt={producto.name} />
                </ItemDetalle> : <NotFound />}
            </div>
        </>

    }
    else if (consola) {
        const aux = producto.consolas.find(producto => producto.id.toString() === consola);

        return <>
            <div >
                {(aux !== undefined) ? <ItemDetalle producto={aux}>
                    <img className='imgProductosDetalle' src={aux.url} alt={aux.name} />
                </ItemDetalle> : <NotFound />}
            </div>
        </>
    }
    else {
        const aux = producto.juegos.find(producto => producto.id.toString() === juego);

        return <>
            <div >
                {(aux !== undefined) ? <ItemDetalle
                    producto={aux}>
                    <img className='imgProductosDetalle'
                        src={aux.url}
                        alt={aux.name} />
                </ItemDetalle> : <NotFound />}
            </div>
        </>
    }

}