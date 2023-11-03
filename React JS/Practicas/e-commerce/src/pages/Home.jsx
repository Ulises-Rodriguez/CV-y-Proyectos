import React from 'react'
import { Item } from '../components/Item';
import { ItemListContainer } from '../components/ItemListContainer';
import { Loading } from '../components/Loading';
import { useGetFSC } from '../customHooks/useGetFSColecction';
import { cargar } from '../funJS/cargar';


export const Home = () => {

    const {loading} = cargar();

    const {productos} = useGetFSC("juegosRetro");

    return (
        <>
            {loading ? <div>
                <ItemListContainer mensaje="Bienvenido a la tienda!!!" />
                <div className='divUlCardsContainer'>
                    <ul className='ulCards'>
                        {productos.map((producto) => <Item
                            key={producto.id}
                            url={`${producto.id}`}
                            titulo={producto.name}
                            descripcion={producto.descripcion}
                            precio={producto.precio}
                            stock={producto.stock}>
                            <img className='imgProductos' src={producto.url} alt={producto.name} />
                        </Item>)}
                    </ul>
                </div>
            </div> : <Loading />}
        </>
    )
}
