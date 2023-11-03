import React from 'react'
import { useParams } from 'react-router-dom'
import { Item } from '../components/Item';
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { Loading } from '../components/Loading';
import { cargar } from '../funJS/cargar';
import { NotFound } from './NotFound';

export const JuegosDetalles = () => {

    const { id } = useParams();
    
    const {productos} = useGetFSC("juegos");

    const {loading} = cargar();

    const obtenerProducto = (id) => {
        return productos.find(producto => producto.id === id);
    }

    const productoElegido = obtenerProducto(id);

    return (
        <>
            {loading ? <div className='divUlCardsContainer'>
                <ul className='ulCards'>
                    {(productoElegido !== undefined) ? productoElegido.juegos.map((juego) => <Item
                        key={juego.id}
                        url={`juegos/${id}/${juego.id}`}
                        titulo={juego.name}
                        descripcion={juego.descripcion}
                        precio={juego.precio}
                        style={{ width: "18rem", height: "740px" }}
                        stock={juego.stock}>
                        <img className='imgProductos' src={juego.url} alt={juego.name} />
                    </Item>) : <NotFound />}
                </ul>
            </div> : <Loading />}
        </>
    )
}
