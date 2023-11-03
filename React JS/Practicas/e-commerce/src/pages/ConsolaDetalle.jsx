import React from 'react'
import { useParams } from 'react-router-dom'
import { Item } from '../components/Item';
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { cargar } from '../funJS/cargar';
import { Loading } from '../components/Loading';
import { NotFound } from './NotFound';

export const ConsolaDetalle = () => {
    const { id } = useParams();
    // DATO PARA MI MISMO POR ALGUN MOTIVO HAY VECES EN LAS Q LA RUTA FUNCIONA CON . --> './.../...
    //POR ALGUN MOTIVO DENTRO DE CONSOLADETALLES.JSX NO
    //CREO Q SE DEBE A LAS <ROUTE PATH=/CONSOLA/:ID>
    //XQ SI LO PONES <ROUTE PATH=/XBOX> PONER CADA CONSOLA CON SU PROPIA RUTA Y NO COMO SUBRUTA ANDA BIEN
    // const { productos } = useFetch('/consolas/consolas.json');

    const {loading} = cargar();

    const {productos} = useGetFSC("consolas");

    const obtenerProducto = (id) => {
        return productos.find(producto => producto.id === id);
    }

    const productoElegido = obtenerProducto(id);

    return (
        <>
            {loading ? <div className='divUlCardsContainer'>
                <ul className='ulCards'>
                    {(productoElegido !== undefined) ? productoElegido.consolas.map((consolaProduct) => <Item 
                    key={consolaProduct.id}
                    url={`consolas/${id}/${consolaProduct.id}`}
                    titulo={consolaProduct.name} 
                    descripcion={consolaProduct.descripcion} 
                    precio={consolaProduct.precio}
                    style={{width : "18rem",height : "710px"}}
                    stock={consolaProduct.stock}>
                        <img className='imgProductos' src={consolaProduct.url} alt={consolaProduct.consola} />
                    </Item>) : <NotFound />}
                </ul>
            </div> : <Loading />}
        </>
    )
}
