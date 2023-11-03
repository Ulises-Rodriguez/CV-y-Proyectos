import React from 'react';
import { Item } from '../components/Item';
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { Loading } from '../components/Loading';
import { cargar } from '../funJS/cargar';

export const Figuras = () => {

    const {loading} = cargar();

    const {productos} = useGetFSC("figuras");

    return (
        <>
            {loading ? <div className='divUlCardsContainer'>
                <ul className='ulCards'>
                    {productos && productos.map((figura) => <Item 
                    key={figura.id} 
                    url={`figuras/${figura.id}`}
                    titulo={figura.name} 
                    descripcion={figura.descripcion} 
                    precio={figura.precio}
                    style={{width : "18rem",height : "510px"}}
                    stock={figura.stock}>
                        <img className='imgProductos' src={figura.url} alt={figura.name} />
                    </Item>)}
                </ul>
            </div> : <Loading />}
        </>
    )
}
